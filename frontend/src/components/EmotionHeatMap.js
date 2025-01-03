import React, { useState, useEffect, useRef } from 'react';
import * as d3 from "d3";

const EmotionHeatMap = ({ results }) => {
  // Initialize hooks first, before any conditional logic
  const [data, setData] = useState([]);
  const svgRef = useRef(null);

  // Use useEffect hooks to process data and create the heatmap
  useEffect(() => {
    // Check if results exist, otherwise return early (skip data processing)
    if (!results || !results.paragraphs) {
      return; // Skip if no results are available
    }

    // Flatten the data into a format suitable for the heatmap
    const aggregatedData = results.paragraphs.map((paragraph, paraIndex) => {
      return paragraph.sentences.flatMap((sentence) => {
        return sentence.clauses.map((clause) => {
          // Ensure each entry includes the time (paraIndex), emotion, and intensity
          return {
            time: paraIndex + 1, // Use paraIndex as the time step
            emotion: Object.keys(clause.emotions), // Get all emotions for this clause
            intensity: Object.values(clause.emotions) // Get corresponding intensity values
          };
        });
      });
    });

    // Flatten the array and set it to the state
    setData(aggregatedData.flat());
  }, [results]);

  useEffect(() => {
    if (data.length === 0) return;

    const width = 1000;
    const height = 500;
    const margin = { top: 20, right: 20, bottom: 40, left: 40 };

    // List of all 38 emotions
    const emotions = [
      "admiration", "amusement", "anger", "annoyance", "approval", "boredom", "calmness",
      "caring", "courage", "curiosity", "desire", "despair", "disappointment", "disapproval",
      "disgust", "doubt", "embarrassment", "envy", "excitement", "faith", "fear",
      "frustration", "gratitude", "greed", "grief", "guilt", "indifference", "joy",
      "love", "nervousness", "nostalgia", "optimism", "pain", "pride", "relief",
      "sadness", "surprise", "trust"
    ];

    const timeSteps = [...new Set(data.map((d) => d.time))]; // Ensure time steps are correct

    const xScale = d3.scaleBand()
      .domain(timeSteps) // Ensure time steps are correctly mapped
      .range([margin.left, width - margin.right])
      .padding(0.05);

    const yScale = d3.scaleBand()
      .domain(emotions) // Use all emotions on the y-axis
      .range([margin.top, height - margin.bottom])
      .padding(0.1);

    const colorScale = d3.scaleSequential(d3.interpolateBlues)
      .domain([0, 1]); // Map intensity values from 0 to 1 for color

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height);

    svg.selectAll("*").remove(); // Clear previous render

    // Draw grid lines for x (time) and y (emotion)
    svg.selectAll(".x-grid")
      .data(timeSteps)
      .enter().append("line")
      .attr("x1", (d) => xScale(d))
      .attr("x2", (d) => xScale(d))
      .attr("y1", margin.top)
      .attr("y2", height - margin.bottom)
      .attr("stroke", "#ccc")
      .attr("stroke-width", 1);

    svg.selectAll(".y-grid")
      .data(emotions)
      .enter().append("line")
      .attr("x1", margin.left)
      .attr("x2", width - margin.right)
      .attr("y1", (d) => yScale(d))
      .attr("y2", (d) => yScale(d))
      .attr("stroke", "#ccc")
      .attr("stroke-width", 1);

    // Render the heatmap cells for all emotions
    svg.selectAll("rect")
      .data(data.flatMap(d => d.emotion.map((e, i) => ({
        time: d.time,
        emotion: e,
        intensity: d.intensity[i]
      })))) // Flatten out the emotion list to get individual cells
      .enter().append("rect")
      .attr("x", (d) => xScale(d.time)) // X-axis (time)
      .attr("y", (d) => yScale(d.emotion)) // Y-axis (emotion labels)
      .attr("width", xScale.bandwidth()) // Width of each cell
      .attr("height", yScale.bandwidth()) // Height of each cell (based on emotion)
      .attr("fill", (d) => colorScale(d.intensity)) // Color based on intensity
      .attr("stroke", "#ddd") // Border color for checkered effect
      .attr("stroke-width", 0.5) // Border width for the grid
      .append("title")
      .text((d) => `${d.emotion}: ${d.intensity}`); // Tooltip showing emotion and intensity

    // Add labels for the x-axis (time)
    svg.selectAll(".x-axis-label")
      .data(timeSteps)
      .enter().append("text")
      .attr("x", (d) => xScale(d) + xScale.bandwidth() / 2) // Position at the center of each time step
      .attr("y", height - margin.bottom + 20) // Position below the x-axis grid
      .attr("text-anchor", "middle")
      .text((d) => d); // Time step label

    // Add labels for the y-axis (emotions)
    svg.selectAll(".y-axis-label")
      .data(emotions)
      .enter().append("text")
      .attr("x", margin.left - 10) // Position to the left of the grid
      .attr("y", (d) => yScale(d) + yScale.bandwidth() / 2) // Position in the center of each emotion row
      .attr("text-anchor", "end")
      .attr("alignment-baseline", "middle")
      .text((d) => d); // Emotion label

  }, [data]);

  // Early return logic moved after hooks
  if (!results || !results.paragraphs) {
    return (
      <div className="p-6 bg-white rounded-lg shadow-md">
        <h3 className="text-xl font-semibold text-gray-800">No Results Available</h3>
        <p>Please submit text for analysis.</p>
      </div>
    );
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md space-y-6">
      <h3 className="text-xl font-semibold text-gray-800">Emotion Heat Map</h3>

      <div>
        <h2>Emotion Heatmap</h2>
        <svg ref={svgRef}></svg>
      </div>
    </div>
  );
};

export default EmotionHeatMap;
