import 'flowbite';
import React from 'react';

const ParameterControls = () => {
  return (
    <div className="p-6 bg-white rounded-lg shadow-md space-y-4">
      <h3 className="text-xl font-semibold text-gray-800">Parameter Controls</h3>
      {/* Emotion Threshold Slider */}
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Emotion Threshold
        </label>
        <input
          type="range"
          min="0"
          max="1"
          step="0.1"
          className="w-full mt-2"
        />
      </div>
      {/* Granularity Toggles */}
      <div className="flex justify-between">
        <button className="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 focus:ring-2 focus:ring-gray-300">
          Clause
        </button>
        <button className="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 focus:ring-2 focus:ring-gray-300">
          Sentence
        </button>
        <button className="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 focus:ring-2 focus:ring-gray-300">
          Full Text
        </button>
      </div>
    </div>
  );
};

export default ParameterControls;
