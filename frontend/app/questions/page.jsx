"use client";
import React, { useState } from "react";
import MultipleChoice from "@/components/MultipleChoice";
import LongAnswer from "@/components/LongAnswer";
import useStore from "@/store/store";

function page() {
  const [hasCompleted, setHasCompleted] = useState(false);
  const [formData, setFormData] = useState({});
  const [correctAnswers, setCorrectAnswers] = useState(0);
  const allQuestions = useStore((state) => state.questions);

  function getNumQuestions() {
    let numQuestions = 0;
    for (const topic in allQuestions) {
      numQuestions += allQuestions[topic].length;
    }
    return numQuestions;
  }

  const handleInputChange = (topic, idx, value) => {
    const questionObj = allQuestions[topic][idx];
    const isCorrect = value === questionObj.answer.correct_idx;

    setFormData((prevData) => {
      const prevIsCorrect = prevData[`${topic}-${idx}`]?.isCorrect || false;
      const newFormData = {
        ...prevData,
        [`${topic}-${idx}`]: {
          value,
          isCorrect,
        },
      };

      setCorrectAnswers((prevCorrectAnswers) => {
        if (prevIsCorrect && !isCorrect) {
          return prevCorrectAnswers - 1;
        } else if (!prevIsCorrect && isCorrect) {
          return prevCorrectAnswers + 1;
        } else {
          return prevCorrectAnswers;
        }
      });

      return newFormData;
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Collected Form Data: ", formData);
    setHasCompleted(true);
  };

  return (
    <div className="space-y-4">
      {/* Result Modal */}
      <div
        className={`fixed  ${
          hasCompleted ? "translate-y-0" : "translate-y-full"
        } top-0 left-0 h-screen w-full bg-violet-500 z-20 duration-200 ease-in flex flex-col justify-center items-center`}
      >
        <div className="flex flex-col text-center">
          <h1 className="text-4xl">🎉</h1>
          <h1 className="text-4xl font-semibold">Amazing job!</h1>
          You got {correctAnswers} questions right and {getNumQuestions() - correctAnswers} questions wrong for a total of {Math.round(correctAnswers / getNumQuestions() * 100)}%
        </div>
      </div>

      {/* Header */}
      <div className="p-8">
        <h1 className="text-5xl font-semibold text-violet-500">
          Question time ✏️
        </h1>
        <p className="text-xl">
          Based on your study habits, we compiled these questions:
        </p>
      </div>
      <div className="w-full h-[1px] bg-violet-500"></div>

      {/* Form */}
      <form onSubmit={handleSubmit}>
        <div className="flex flex-col space-y-4 divide-y-[1px] divide-violet-500">
          {Object.keys(allQuestions).map((topic, idx) => (
            <div key={topic}>
              <h2 className="text-2xl font-semibold">{topic}</h2>
              {allQuestions[topic].map((cur_question, jdx) => (
                <div key={`${topic}-${jdx}`}>
                  {cur_question.long == 1 ? (
                    <LongAnswer
                      key={`${topic}-${jdx}`}
                      question={cur_question.question}
                      answer={cur_question.answer}
                    />
                  ) : (
                    <MultipleChoice
                      key={`${topic}-${jdx}`}
                      name={`${topic}-${jdx}`}
                      question={cur_question.question}
                      answerContent={cur_question.answer.options}
                      correct={cur_question.answer.correct_idx}
                      onChange={(value) => handleInputChange(topic, jdx, value)}
                    />
                  )}
                </div>
              ))}
            </div>
          ))}
        </div>
        <button
          type="submit"
          className="fixed bottom-0 left-0 h-16 bg-violet-600 font-semibold w-full hover:bg-violet-500 duration-100"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default page;
