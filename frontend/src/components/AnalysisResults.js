import 'flowbite';
import React from 'react';

const AnalysisResults = ({ results }) => {
  return (
    <div className="p-6 bg-white rounded-lg shadow-md space-y-6">
      <h3 className="text-xl font-semibold text-gray-800">Results</h3>
      {/* Line Graph Placeholder */}
      <div className="w-full h-40 bg-gray-100 rounded-lg flex items-center justify-center">
        <p className="text-gray-500">[Line Graph Placeholder]</p>
      </div>
      {/* Bar Chart Placeholder */}
      <div className="w-full h-40 bg-gray-100 rounded-lg flex items-center justify-center">
        <p className="text-gray-500">[Bar Chart Placeholder]</p>
      </div>
    </div>
  );
};

export default AnalysisResults;
