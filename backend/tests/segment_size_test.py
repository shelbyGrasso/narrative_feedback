from backend.src.app.text_processor import segment_text
from backend.src.app.emotion_analyzer import analyze_emotion
import json


def analyze_by_clauses(text):
    """
    Analyze text by segmenting it into clauses and detecting emotions for each clause.

    Args:
        text (str): The input text.

    Returns:
        list: A list of clauses with their detected emotions.
    """
    segmented = segment_text(text)
    results = []

    for paragraph in segmented:
        for sentence in paragraph["sentences"]:
            for clause in sentence["clauses"]:
                emotions = analyze_emotion(clause["text"])
                results.append({
                    "text": clause["text"],
                    "emotions": emotions
                })

    return results


def analyze_full_text(text):
    """
    Analyze the entire text as a single chunk.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary of emotions for the full text.
    """
    return analyze_emotion(text)


if __name__ == "__main__":
    # Sample texts
    texts = {
        "Text 1": "She was happy, but she felt nervous.",
        "Text 2": "He smiled and said nothing.",
        "Text 3": "You liked my green shirt. You never told me so – you weren’t one to tell me you liked things about me (or that you liked me). But I know you liked it because at the end of the night – when everyone had gone home, and I’d had just one too many drinks, and you were being the gentleman you so desperately wanted to be by waiting patiently while I dumped the contents of abandoned bottles down the drain and filled a trash bag with enough plastic cups to turn myself into a disgusted environmentalist for just a moment – you got handsy.",
        "Text 4": "“I DON'T CARE!\" Harry yelled at them, snatching up a lunascope and throwing it into the fireplace. "
    "\"I'VE HAD ENOUGH, I'VE SEEN ENOUGH, I WANT OUT, I WANT IT TO END, I DON'T CARE ANYMORE!\"\n"
    "\"You do care,\" said Dumbledore. He had not flinched or made a single move to stop Harry demolishing his office. "
    "His expression was calm, almost detached. \"You care so much you feel as though you will bleed to death with the pain of it.”"

    }

    for title, full_text in texts.items():
        print(f"\n===== {title} =====")

        # Analyze by clauses
        print("\nAnalyzing by clauses:")
        clause_results = analyze_by_clauses(full_text)
        print(json.dumps(clause_results, indent=4))

        # Analyze as full text
        print("\nAnalyzing full text:")
        full_text_emotions = analyze_full_text(full_text)
        print(json.dumps(full_text_emotions, indent=4))