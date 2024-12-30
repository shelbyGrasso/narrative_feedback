import React, { useState } from 'react';
import TextInput from './components/TextInput';
import ParameterControls from './components/ParameterControls';
import AnalysisResults from './components/AnalysisResults';

const App = () => {
  const [text, setText] = useState("");
  const [results, setResults] = useState({ segments: [] });

  return (
      <div className="min-h-screen bg-gradient-to-b from-beige via-beige to-gray-100 flex flex-col items-center">
          {/* Header */}
          <header className="w-full py-6 bg-walnut-brown text-beige shadow-md">
              <h1 className="text-center text-3xl font-bold tracking-wide">
                  Narrative Feedback Tool
              </h1>
          </header>


          {/* Main Content */}
          <main className="container mx-auto px-8 py-10 space-y-8">
              <TextInput onSubmit={setText}/>
              <ParameterControls/>
              <AnalysisResults results={results}/>
          </main>
      </div>
  );
};

export default App;
