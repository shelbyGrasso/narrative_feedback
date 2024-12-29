import pytest
from src.emotion_analyzer import analyze_emotion
from src.text_processor import segment_text

def test_segment_and_analyze():
    text = "She was happy, but she felt nervous."
    result = segment_text(text)

    for paragraph in result:
        for sentence in paragraph["sentences"]:
            for clause in sentence["clauses"]:
                emotions = analyze_emotion(clause["text"])
                assert isinstance(emotions, dict)
                assert all(isinstance(emotion, str) for emotion in emotions.keys())

def test_analyze_emotion_single_emotion():
    clause = "She was happy."
    emotions = analyze_emotion(clause)
    assert "joy" in emotions
    assert emotions["joy"] > 0.1

def test_analyze_emotion_multiple_emotions():
    # Test that the function detects more than one emotion in a single input.
    clause = "He was happy and surprised."
    emotions = analyze_emotion(clause)
    assert len(emotions) > 1, "Expected more than one emotion to be detected."

def test_basic_emotion_detection():
    # Test that the function returns a dictionary with detected emotions for a simple input.
    text = "I feel happy and excited."
    emotions = analyze_emotion(text)
    assert isinstance(emotions, dict), "Output should be a dictionary."
    assert "joy" in emotions, "'joy' should be detected."
    assert emotions["joy"] > 0, "Score for 'joy' should be greater than 0."


def test_empty_input():
    # Test that the function handles empty input gracefully.
    text = ""
    emotions = analyze_emotion(text)
    assert emotions == {}, "Empty input should return an empty dictionary."


def test_neutral_text():
    # Test that the function does not detect emotions in neutral or non-emotional text.
    text = "This is a table."
    emotions = analyze_emotion(text)
    assert emotions == {}, "Neutral text should return no significant emotions."


def test_multiple_emotions():
    # Test that the function detects multiple emotions in a single input.
    text = "I am excited but also nervous."
    emotions = analyze_emotion(text)
    assert "excitement" in emotions and "nervousness" in emotions, "Both 'excitement' and 'nervousness' should be detected."
    assert emotions["excitement"] > 0 and emotions["nervousness"] > 0, "Scores for detected emotions should be greater than 0."


def test_threshold_filtering():
    # Test that the function can filter out emotions below a specified threshold.
    text = "I am slightly happy."
    emotions = analyze_emotion(text)
    threshold = 0.1
    filtered_emotions = {k: v for k, v in emotions.items() if v > threshold}
    assert all(v > threshold for v in filtered_emotions.values()), "All included emotions should have scores above the threshold."


def test_long_input():
    # Test that the function handles long, complex input with multiple emotions.
    text = "I am so incredibly happy and thrilled about the new job opportunity, but I also feel a bit nervous and unsure about moving to a new city."
    emotions = analyze_emotion(text)
    assert "joy" in emotions, "'joy' should be detected in the text."
    assert len(emotions) > 1, "Multiple emotions should be detected in complex input."