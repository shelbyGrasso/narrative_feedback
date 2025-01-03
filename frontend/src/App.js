import React, { useState } from "react";
import TextInput from "./components/TextInput";
import ParameterControls from "./components/ParameterControls";
import AnalysisResults from "./components/AnalysisResults";
import EmotionHeatMap from "./components/EmotionHeatMap";

const App = () => {
  const [results, setResults] = useState({ paragraphs: [] }); // Default structure
  const [rawData, setRawData] = useState({ paragraphs: [] }); // To hold all emotions
  const [threshold, setThreshold] = useState(0.5); // State for threshold slider

  const analyzeText = async (text) => {
    const payload = {
      text: text,
      threshold: 0, // Convert threshold to a float
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
      console.log("Backend response received:", data); // Log backend response

      setRawData(data); // Save raw data for recomputation
      setResults(data); // Update results for display
      console.log("Raw data set:", data);
      recomputeText(threshold, data);
    } catch (error) {
      console.error("Error analyzing text:", error);
    }
  };

  const recomputeText = (newThreshold, rawDataOverride = rawData) => {
console.log("Recomputing results with threshold:", newThreshold);

    const sourceData = rawDataOverride || rawData; // Use provided data or fallback to state
console.log("Raw data for recomputation:", sourceData);
    if (!sourceData || !sourceData.paragraphs) {
      console.error("No raw data available for recomputation.");
      return;
    }

    const filteredResults = sourceData.paragraphs.map((paragraph) => ({
    ...paragraph,
    sentences: paragraph.sentences.map((sentence) => ({
      ...sentence,
      clauses: sentence.clauses.map((clause) => {
        const filteredEmotions = Object.fromEntries(
          Object.entries(clause.emotions).filter(
            ([emotion, score]) => score >= newThreshold
          )
        );
        console.log("Original emotions:", clause.emotions);
        console.log("Filtered emotions:", filteredEmotions);
        return {
          ...clause,
          emotions: filteredEmotions,
        };
      }),
    })),
  }));

    // Update the results state with recomputed data
    console.log("Updated results:", filteredResults);
    setResults({ paragraphs: filteredResults });
  };

  return (
  <div className="min-h-screen bg-gradient-to-b from-beige via-beige to-gray-100 flex flex-col items-center">
    <header className="w-full py-6 bg-walnut-brown text-beige shadow-md">
      <h1 className="text-center text-3xl font-bold tracking-wide">
        Narrative Feedback Tool
      </h1>
    </header>

    <main className="container mx-auto px-8 py-10 space-y-8">
      {/* Flex container for TextInput and ParameterControls */}
      <div className="flex flex-col md:flex-row justify-between space-y-6 md:space-y-0 md:space-x-6">
        {/* TextInput */}
        <div className="w-full md:w-1/2">
          <TextInput onSubmit={(text) => analyzeText(text)} />
        </div>

        {/* ParameterControls */}
        <div className="w-full md:w-1/2">
          <ParameterControls
            threshold={threshold}
            onChange={(newThreshold) => {
              setThreshold(newThreshold); // Update local state
              recomputeText(newThreshold); // Dynamically recompute results
            }}
          />
        </div>
      </div>

      {/* AnalysisResults */}
      <AnalysisResults results={results} />
      <EmotionHeatMap results={results} />
    </main>
  </div>
  );

};

export default App;
