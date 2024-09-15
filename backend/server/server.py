import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)

import json
import flask
import dotenv
import tempfile
import cohere
from cohere import ResponseFormat_JsonObject as R
from pathlib import Path
from flask_cors import cross_origin
from jsonschema import validate, ValidationError
import PyPDF2
from screen_recorder.NotesFixer import main as begin_screen_recording
from multiprocessing import Process
from screen_recorder.overlay import engage_overlay

# /syllabus endpoint (with syllabus)
# /package endpoint (with chunks of course info)
dotenv.load_dotenv()

API_KEY = os.environ.get("COHERE_API_KEY")


chat_history = None
co = cohere.Client(API_KEY)
preamble = None
question_pool = {}
overlay_process = Process(target=engage_overlay)


def verify_question(question, answer):
    co = cohere.Client(API_KEY)
    preamble = Path("preambles/verify.txt").read_text()
    response = co.chat(
        model="command-r-plus-08-2024",
        message=f"QUESTION: {question}\n\nANSWER: {answer}",
        preamble=preamble,
        response_format=R(),
    )
    print(response.text)

    return True if response.text == "YES" else False


def make_flask_app():
    app = flask.Flask(__name__)

    with open(os.path.join(cur_dir, "schema.json"), "r") as f:
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

        syllabus_text = ""
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, filename), "wb+") as f:
                syllabus_data = flask.request.get_data()
                f.write(syllabus_data)
                f.flush()
                read_pdf = PyPDF2.PdfReader(f)
                for page in read_pdf.pages:
                    syllabus_text += page.extract_text()

        print("Parsed syllabus")
        # initialize the preamble
        with open(os.path.join(cur_dir, "preambles/questions.txt"), "r") as f:
            preamble_text = f.read()
            preamble = f"{preamble_text}\n\n\n---\n\n\n The syllabus is as follows:\n{syllabus_text}"

        Process(target=begin_screen_recording).start()
        overlay_process.start()
        print("Started screen recording")

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
                print("Asking Cohere")
                response = co.chat(
                    preamble=preamble,
                    chat_history=chat_history,
                    message=packaged_text,
                    model="command-r-plus-08-2024",
                    response_format={"type": "json_object"},
                )

                text = json.loads(response.text)

                validate(text, schema)
                chat_history = response.chat_history

                break
            except (ValidationError, json.JSONDecodeError) as e:
                print(e)
                continue

        question_pool.update(text)
        print(question_pool)

        return "Success", 200

    @app.route("/question", methods=["GET"])
    @cross_origin()
    def question():
        overlay_process.terminate()
        return json.dumps(question_pool)

    @app.route("/")
    def root():
        return "poop"

    return app


def main():
    print("Starting server")
    app = make_flask_app()
    app.run(host="0.0.0.0", port=3001)


if __name__ == "__main__":
    main()
