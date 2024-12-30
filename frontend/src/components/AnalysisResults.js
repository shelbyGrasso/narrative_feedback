import React from 'react';

const AnalysisResults = ({ results }) => {
  console.log("Rendering AnalysisResults with results:", results); // Debugging log

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
      <h3 className="text-xl font-semibold text-gray-800">Results</h3>

      {results.paragraphs.map((paragraph, paraIndex) => (
        <div key={paraIndex} className="space-y-4">
          <h4 className="text-lg font-medium text-gold">Paragraph {paraIndex + 1}</h4>

          {paragraph.sentences.map((sentence, sentIndex) => (
            <div key={sentIndex} className="pl-4 border-l-4 border-gold">
              <p className="text-gray-800">
                <strong>Sentence {sentIndex + 1}:</strong> {sentence.text}
              </p>

              <ul className="pl-4">
                {sentence.clauses.map((clause, clauseIndex) => (
                  <li key={clauseIndex} className="list-disc text-gray-700">
                    Clause {clauseIndex + 1}: {clause.text} {/* Render the text property */}
                    <ul className="pl-4">
                      <li>
                        Relationship: {clause.relationship}
                      </li>
                      <li>
                        Emotions: {JSON.stringify(clause.emotions)}
                      </li>
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default AnalysisResults;
