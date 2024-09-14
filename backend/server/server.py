import os
import json
import flask
import dotenv
import tempfile
import cohere
from cohere import ResponseFormat_JsonObject as R
from pathlib import Path
from llama_parse import LlamaParse, ResultType
from flask_cors import cross_origin
from jsonschema import validate, ValidationError

# /syllabus endpoint (with syllabus)
# /package endpoint (with chunks of course info)

API_KEY = os.environ.get("COHERE_API_KEY")


chat_history = None
dotenv.load_dotenv()
co = cohere.Client(API_KEY)
preamble = None
question_pool = {}


def verify_question(question, answer):
    co = cohere.Client(API_KEY)
    preamble = Path("preambles/verify.txt").read_text()


def make_flask_app():
    app = flask.Flask(__name__)

    with open("schema.json", "r") as f:
        schema = json.load(f)

    @app.route("/syllabus", methods=["POST"])
    @cross_origin()
    def syllabus():
        # method to initialize Cohere with the preamble and syllabus pdf. We r assuming that
        # we get an octet stream w the syllabus inside
        global preamble

        content_type = flask.request.headers.get("Content-Type")
        filename = flask.request.headers.get("sessions-filename")
        if not content_type or not filename:
            return (
                json.dumps(
                    {"error": "Content-Type and sessions-filename headers are required"}
                ),
                400,
            )

        if content_type != "application/octet-stream":
            return (
                json.dumps({"error": "Content-Type must be application/octet-stream"}),
                400,
            )

        # parse the syllabus
        print("Parsing syllabus")

        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, filename), "wb") as f:
                syllabus_data = flask.request.get_data()
                parser = LlamaParse(result_type=ResultType.TXT)
                f.write(syllabus_data)
                syllabus = parser.load_data(os.path.join(temp_dir, filename))
        print("Parsed syllabus")

        # initialize the preamble
        with open("preambles/questions.txt", "r") as f:
            preamble_text = f.read()
            preamble = f"{preamble_text}\n\n\n---\n\n\n The syllabus is as follows:\n{syllabus}"

        return "Success", 200

    @app.route("/package", methods=["POST"])
    @cross_origin()
    def package():
        global preamble, chat_history

        content_type = flask.request.headers.get("Content-Type")
        if not content_type or "text/plain" not in content_type:
            return (
                json.dumps({"error": "Content-Type must be text/plain"}),
                400,
            )

        # parse the packaged notes/study materials
        print("Parsing packaged notes")
        packaged_text = flask.request.get_data().decode("utf-8")

        print(packaged_text)

        text = {}

        while True:
            try:
                response = co.chat(
                    preamble=preamble,
                    chat_history=chat_history,
                    message=packaged_text,
                    model="command-r-plus-08-2024",
                    response_format=R(),
                )

                text = json.loads(response.text)

                validate(text, schema)
                chat_history = response.chat_history

                break
            except (ValidationError, json.JSONDecodeError):
                continue

        question_pool.update(text)
        print(question_pool)

        return "Success", 200

    @app.route("/question", methods=["GET"])
    @cross_origin()
    def question():
        return json.dumps(question_pool)

    @app.route("/")
    def root():
        return "poop"

    return app


def main():
    app = make_flask_app()
    app.run(host="0.0.0.0", port=3001)


if __name__ == "__main__":
    main()
