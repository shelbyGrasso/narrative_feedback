import React, { useState } from "react";
import TextInput from "./components/TextInput";
import ParameterControls from "./components/ParameterControls";
import AnalysisResults from "./components/AnalysisResults";

const App = () => {
  const [results, setResults] = useState({ segments: [], emotions: {} }); // Default structure
  const [threshold, setThreshold] = useState(0.5); // State for threshold slider

  const analyzeText = async (text) => {
  const payload = {
    text: text,
    threshold: parseFloat(threshold), // Convert threshold to a float
  };

  console.log("Payload being sent:", payload);

  try {
    const response = await fetch("http://localhost:8000/analyze/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload), // Convert to JSON string
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }

    const data = await response.json();
    setResults(data); // Update results with backend response
  } catch (error) {
    console.error("Error analyzing text:", error);
  }
};

  return (
    <div className="min-h-screen bg-gradient-to-b from-beige via-beige to-gray-100 flex flex-col items-center">
      <header className="w-full py-6 bg-walnut-brown text-beige shadow-md">
        <h1 className="text-center text-3xl font-bold tracking-wide">
          Narrative Feedback Tool
        </h1>
      </header>

      <main className="container mx-auto px-8 py-10 space-y-8">
        <TextInput onSubmit={(text) => analyzeText(text)} />
        <ParameterControls
          threshold={threshold}
          onChange={(newThreshold) => {
            setThreshold(newThreshold); // Update local state
          }}
        />
        <AnalysisResults results={results} /> {/* Pass results to AnalysisResults */}
      </main>
    </div>
  );
};

export default App;
