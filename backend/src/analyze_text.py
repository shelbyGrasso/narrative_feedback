from backend.src.text_processor import segment_text
from backend.src.emotion_analyzer import analyze_emotion
import json

def analyze_text_with_emotions(text):
    segmented_text = segment_text(text)
    result = {"paragraphs": []}

    for paragraph_data in segmented_text:
        paragraph = {
            "id": paragraph_data["paragraph"],  # Paragraph ID
            "sentences": []
        }

        for sentence_data in paragraph_data["sentences"]:
            sentence = {
                "text": sentence_data["text"],
                "clauses": []
            }

            for clause_data in sentence_data["clauses"]:
                emotions = analyze_emotion(clause_data["text"])
                clause = {
                    "text": clause_data["text"],
                    "relationship": clause_data["relationship"],
                    "emotions": emotions
                }
                sentence["clauses"].append(clause)

            paragraph["sentences"].append(sentence)

        result["paragraphs"].append(paragraph)

    print(result)
    return result


if __name__ == "__main__":
    text = (
        "She was happy, but she felt nervous. He smiled and said nothing.\n\n"
        "The sun was shining brightly, and the birds were singing."
    )
    print("Input Text:\n")
    print(text)

    print("\nAnalyzing text...\n")
    try:
        # Analyze the text
        result = analyze_text_with_emotions(text)

        # Pretty-print the result
        print("Analysis Results:\n")
        print(json.dumps(result, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
