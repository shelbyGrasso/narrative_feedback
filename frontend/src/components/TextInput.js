import 'flowbite';
import React, { useState } from 'react';

const TextInput = ({ onSubmit }) => {
  const [text, setText] = useState("");

  const handleSubmit = () => {
    onSubmit(text);
    setText("");
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
            <div className="flex space-x-4">
                <button
                    className="px-4 py-2 bg-walnut-brown text-beige rounded-lg shadow hover:bg-gold hover:text-walnut-brown focus:ring-2 focus:ring-gold"
                    onClick={handleSubmit}
                >
                    Submit
                </button>
                <button
                    className="px-4 py-2 bg-walnut-brown text-beige rounded-lg shadow hover:bg-gold hover:text-walnut-brown focus:ring-2 focus:ring-gold"
                    onClick={() => setText("Sample text for demonstration.")}
                >
                    Load Example
                </button>
            </div>
        </div>
    </div>
  );
};

export default TextInput;
