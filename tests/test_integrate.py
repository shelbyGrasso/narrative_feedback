from src.analyze_text import analyze_text_with_emotions

def test_analyze_text_with_emotions():
    # Input text
    text = "She was happy, but she felt nervous. He smiled and said nothing."

    # Run the function
    result = analyze_text_with_emotions(text)

    # Assertions
    assert "paragraphs" in result, "Result should contain paragraphs."
    assert len(result["paragraphs"]) == 1, "There should be one paragraph."

    paragraph = result["paragraphs"][0]
    assert "sentences" in paragraph, "Paragraph should contain sentences."
    assert len(paragraph["sentences"]) == 2, "There should be two sentences."

    sentence1 = paragraph["sentences"][0]
    assert "clauses" in sentence1, "Sentence should contain clauses."
    assert len(sentence1["clauses"]) == 2, "First sentence should have two clauses."

    clause1 = sentence1["clauses"][0]
    assert "text" in clause1, "Clause should have a 'text' field."
    assert clause1["text"] == "She was happy", "Clause text should match expected value."
    assert "emotions" in clause1, "Clause should have 'emotions' field."
    assert "joy" in clause1["emotions"], "Clause should contain detected emotions."

    clause2 = sentence1["clauses"][1]
    assert clause2["relationship"] == "contrast", "Second clause should have 'contrast' relationship."
    assert "nervousness" in clause2["emotions"], "Clause should contain detected emotions."

    # Ensure second sentence is handled correctly
    sentence2 = paragraph["sentences"][1]
    assert len(sentence2["clauses"]) == 1, "Second sentence should have one clause."
    assert sentence2["clauses"][0]["text"] == "He smiled and said nothing", "Clause text should match expected value."
