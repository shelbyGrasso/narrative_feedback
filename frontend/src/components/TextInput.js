import React, { useState } from 'react';

const TextInput = ({ onSubmit }) => {
  const [text, setText] = useState("");

  const handleSubmit = () => {
    if (text.trim()) {
      onSubmit(text); // Pass text to onSubmit (API call in App.js)
    }
  };

  return (
    <div className="p-6 bg-white rounded-lg shadow-md space-y-4">
      <textarea
        className="w-full h-40 p-4 text-gray-700 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-400"
        placeholder="Type or paste your text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <div className="flex space-x-4">
        <button
          onClick={handleSubmit}
          className="px-4 py-2 bg-walnut-brown text-beige rounded-lg shadow hover:bg-gold hover:text-walnut-brown focus:ring-2 focus:ring-gold"
        >
          Analyze
        </button>
      </div>
    </div>
  );
};

export default TextInput;
