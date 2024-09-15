import React, { useState } from "react";

function MultipleChoice({ name, answerContent, correct, question, onChange }) {
  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionChange = (e) => {
    const selectedValue = parseInt(e.target.value, 10);
    setSelectedOption(selectedValue);
    onChange(selectedValue);
  };

  return (
    <div className="flex flex-col space-y-2 text-xl relative p-8">
      <p className="text-2xl font-semibold">{question}</p>

      {answerContent.map((mcq, jdx) => (
        <div key={jdx} className="space-x-2">
          <input
            type="radio"
            id={`${name}-${jdx}`}
            name={name} // Unique name for each question
            value={jdx}
            checked={selectedOption === jdx}
            onChange={handleOptionChange}
          />
          <label htmlFor={`${name}-${jdx}`}>{mcq}</label>
        </div>
      ))}
    </div>
  );
}

export default MultipleChoice;
