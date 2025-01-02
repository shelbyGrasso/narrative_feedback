from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
model_name = "lrei/distilroberta-base-emolit"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Emotion labels provided by the model
emotion_labels = [
    "admiration", "amusement", "anger", "annoyance", "approval", "boredom", "calmness",
    "caring", "courage", "curiosity", "desire", "despair", "disappointment", "disapproval",
    "disgust", "doubt", "embarrassment", "envy", "excitement", "faith", "fear",
    "frustration", "gratitude", "greed", "grief", "guilt", "indifference", "joy",
    "love", "nervousness", "nostalgia", "optimism", "pain", "pride", "relief",
    "sadness", "surprise", "trust"
]


def analyze_emotion(text, selected_threshold=0.0):
    """
    Analyze the emotions present in a given text.

    Args:
        text (str): The input text (e.g., a clause).

    Returns:
        dict: A dictionary of detected emotions with their scores above a threshold.
    """
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits

    # Verify output size
    if logits.shape[-1] != len(emotion_labels):
        raise ValueError("Mismatch between model output size and emotion labels.")

    # Apply softmax to get probabilities
    probabilities = torch.softmax(logits, dim=-1).squeeze().tolist()

    # Filter emotions with scores above a threshold (e.g., 0.1)
    threshold = selected_threshold
    emotions = {emotion_labels[i]: prob for i, prob in enumerate(probabilities) if prob > threshold}

    return emotions


if __name__ == "__main__":
    test_clause = "She was happy, but she felt nervous."
    emotions = analyze_emotion(test_clause)
    print(f"Detected emotions: {emotions}")