"use client";
import { useState, useCallback } from "react";
import React from "react";

function LongAnswer({ question, answer }) {
  const [showAi, setShowAi] = useState(false);
  const toggleShowAi = useCallback(() => {
    setShowAi((prevShowAi) => !prevShowAi);
  }, []);
  return (
    <div className="relative p-4 space-y-2 overflow-hidden ">
      <div className="absolute top-0 right-0 p-2 ">
        <button
          type="button"
          onClick={toggleShowAi}
          className="p-3 text-indigo-200 border-[1px] border-white/30 text-sm rounded-xl font-semibold bg-gradient-to-r from-slate-900 via-violet-900 to-slate-900"
        >
          AI answer
        </button>
      </div>
      <p className="text-2xl font-semibold">{question}</p>
      {showAi && (
        <div className="p-3 text-indigo-200 border-[1px] border-white/30 text-sm rounded-xl font-semibold bg-gradient-to-r from-slate-900 via-violet-900 to-slate-900">
          💡 AI's answer: <span className="underline">{answer}</span>
        </div>
      )}
    </div>
  );
}

export default LongAnswer;
