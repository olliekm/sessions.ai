"use client";
import React, { Children, useState } from "react";
import Link from "next/link";
import useStore from "@/store/store";

function page() {
  // Function to start the timer
  const currentQuestions = useStore.getState().questions;

  const [infoSubmitted, setInfoSubmitted] = useState(false);

  const [topics, setTopics] = useState([
    "Cellular respiration",
    "Hemoglobin creation",
    "Historic discoveries about blood",
  ]);

  const [hasStarted, setHasStarted] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  function sendNotification(title, options) {
    if (Notification.permission === "granted") {
      new Notification(title, options);
    } else {
      console.log("Notification permission not granted.");
    }
  }

  // Example usage
  async function fetchQuestions() {
    try {
      const response = await fetch("http://localhost:3001/question", {
        method: "GET",
      });
      const data = await response.json();

      console.log(data);
      setTopics(Object.keys(data));
      useStore.getState().setQuestions(data);
    } catch (err) {
      console.log(err);
    } finally {
    }
  }

  function startTimer(durationInMinutes) {
    const durationInMilliseconds = durationInMinutes * 1000; // Convert minutes to milliseconds
    setHasStarted(true);
    // Set a timeout to trigger after the specified duration
    setTimeout(() => {
      sendNotification("Reminder", {
      body: "Questions are ready for review!",
      });
      fetchQuestions();
      setHasStarted(false);
      setIsPaused(true);
      // You can add any other action you want to perform here
    }, durationInMilliseconds);
  }

  const removeTopic = (topicToRemove) => {
    setTopics((prevTopics) =>
      prevTopics.filter((topic) => topic !== topicToRemove)
    );
    useStore.removeTopic(topicToRemove);
  };

  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState("");

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    // Check if the selected file is a PDF
    if (file && file.type === "application/pdf") {
      setSelectedFile(file);
      setError(""); // Clear any previous errors
    } else {
      setError("Please select a valid PDF file.");
      setSelectedFile(null);
    }
  };

  // Handle file upload
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      setError("Please select a file before submitting.");
      return;
    }

    // Create a FileReader instance
    const reader = new FileReader();

    // Define the onload event handler
    reader.onload = async () => {
      try {
        // The result of the FileReader (ArrayBuffer) will be available in reader.result
        const arrayBuffer = reader.result;
        // Send the ArrayBuffer as the request body
        console.log(arrayBuffer);
        const response = await fetch("http://localhost:3001/syllabus", {
          headers: {
            "Content-Type": "application/octet-stream",
            "sessions-filename": selectedFile.name,
          },
          method: "POST",
          body: arrayBuffer,
        });
        console.log("fafg");

        if (response.ok) {
          console.log("File uploaded successfully");
          startTimer(60);
        } else {
          console.error("File upload failed", response.status);
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    };

    // Define the onerror event handler
    reader.onerror = (error) => {
      console.error("Error reading file:", error);
    };

    // Read the file as an ArrayBuffer
    reader.readAsArrayBuffer(selectedFile);
  };

  if (hasStarted) {
    return (
      <div className="h-full w-full pt-24 text-center justify-center items-center space-y-4">
        <h1 className="text-8xl font-semibold">Studying in progress...</h1>
        <h2 className="text-5xl">Keep it up!</h2>
      </div>
    );
  }

  // Start a 30-minute timer
  if (isPaused) {
    return (
      <div
        className={`flex flex-col justify-center h-full w-full items-center bg-cover bg-[url('https://i.imgur.com/qZFOalA.png')] `}
      >
        <div className=" flex flex-col items-center space-y-4 -mt-32">
          <h1 className="text-6xl font-bold">Great job! 🎉</h1>
          <h2 className="text-2xl italic">You made incredible progress!</h2>
          <h2>Here are your stats:</h2>
          <div className="flex space-x-4">
            <div className="p-10 flex shadow-lg justify-center bg-neutral-900 rounded-xl flex-col items-center">
              <h1 className=" text-xl text-center">Studied for:</h1>
              <h1 className="text-5xl font-bold text-violet-500">5 hours</h1>
            </div>
            <div className="p-8 h-auto shadow-lg w-auto bg-neutral-900 rounded-xl flex justify-center flex-col items-center">
              <h1 className=" text-xl text-center">Focusmeter:</h1>
              <h1 className="text-7xl font-bold text-violet-500">80%</h1>
            </div>
            <div className="p-8 h-auto shadow-lg w-auto bg-neutral-900 rounded-xl flex justify-center flex-col items-center">
              <h1 className=" text-xl text-center">Most relavent topic</h1>
              <h1 className="text-2xl font-bold italic text-violet-500">
                Matrix multiplication
              </h1>
            </div>
          </div>
        </div>
        <div className="bg-neutral-900 flex flex-col text-2xl fixed bottom-0 left-0 w-full p-8">
          <h1>
            Topics we detected:{" "}
            <span className="italic text-sm">{"(click to remove)"}</span>
          </h1>

          <div className="flex justify-between">
            <div className="flex flex-wrap gap-2">
              {topics.length !== 0 ? (
                <>
                  {topics.map((topic, idx) => (
                    <div
                      key={idx}
                      onClick={() => removeTopic(topic)}
                      className="p-2 px-4 rounded-lg w-fit hover:bg-red-700/50 duration-100 bg-neutral-700 flex space-x-2 items-center group cursor-pointer"
                    >
                      <small className="group-hover:line-through">
                        {topic}
                      </small>
                    </div>
                  ))}
                </>
              ) : (
                <div className="">You need to add some</div>
              )}
            </div>
            <Link href={"/questions"}>
              <button className="bg-violet-500 p-4 rounded-xl flex items-center space-x-2">
                <small>Continue to questions</small>
                <svg
                  className="h-6 w-6 fill-white"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 512 512"
                >
                  <path d="M470.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L402.7 256 265.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160zm-352 160l160-160c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L210.7 256 73.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0z" />
                </svg>
              </button>
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex justify-center max-h-screen text-center">
      <div
        className={`fixed top-0 left-0 h-screen w-full bg-violet-600 duration-200 flex justify-center items-center ${
          !infoSubmitted ? "-translate-y-full" : "-translate-y-0"
        }`}
      >
        <div className="space-y-4">
          <h1 className="text-5xl font-bold ">Start your study session!</h1>
          <button
            onClick={handleSubmit}
            className="text-3xl font-semibold rounded-xl bg-neutral-950 text-violet-600 px-8 py-2"
          >
            Start
          </button>
        </div>
      </div>
      <div className=" pt-24 flex flex-col">
        <p className="font-semibold text-7xl w-min text-left">
          It's time to{" "}
          <span className="font-bold italic underline text-violet-500">
            SUPERCHARGE
          </span>{" "}
          your study sessions!
        </p>
        <form method="post" className="flex flex-col space-y-4 pt-10">
          <h1 className="text-left">Enter your information</h1>
          <input
            type="text"
            className="p-4 bg-transparent text-white border-2 border-violet-500 outline-none rounded-2xl"
            placeholder="University"
          />
          <input
            type="text"
            className="p-4 bg-transparent text-white border-2 border-violet-500 outline-none rounded-2xl"
            placeholder="Course code"
          />

          <label
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-left"
            htmlFor="file_input"
          >
            Upload syllabus
          </label>
          <input
            className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            aria-describedby="file_input_help"
            id="file_input"
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
          />
          <p
            className="mt-1 text-sm text-gray-500 dark:text-gray-300 text-left"
            id="file_input_help"
          >
            PDF
          </p>
        </form>
        <div className="w-full h-auto flex justify-center items-center p-8">
          <button
            onClick={() => setInfoSubmitted(true)}
            className="rounded-full w-fit bg-violet-700 group flex justify-center items-center p-6 "
          >
            <svg
              className="fill-neutral-950  w-10 h-10 group-hover:fill-violet-300 duration-150"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 384 512"
            >
              <path d="M73 39c-14.8-9.1-33.4-9.4-48.5-.9S0 62.6 0 80L0 432c0 17.4 9.4 33.4 24.5 41.9s33.7 8.1 48.5-.9L361 297c14.3-8.7 23-24.2 23-41s-8.7-32.2-23-41L73 39z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
}

export default page;
