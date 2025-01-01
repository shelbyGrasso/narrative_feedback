from backend.src.app.analyze_text import analyze_text_with_emotions

def test_analyze_text_with_emotions_paragraphs():
    # Input text with paragraphs
    text = (
        "She was happy, but she felt nervous. He smiled and said nothing.\n\n"
        "The sun was shining brightly, and the birds were singing."
    )

    # Run the function
    result = analyze_text_with_emotions(text)

    # Assertions for paragraphs
    assert "paragraphs" in result, "Result should contain paragraphs."
    assert len(result["paragraphs"]) == 2, "There should be two paragraphs."

    # Test the first paragraph
    paragraph1 = result["paragraphs"][0]
    assert paragraph1["id"] == 1, "First paragraph ID should be 1."
    assert len(paragraph1["sentences"]) == 2, "First paragraph should have two sentences."

    sentence1 = paragraph1["sentences"][0]
    assert sentence1["text"] == "She was happy, but she felt nervous.", "First sentence text should match."

    clause1 = sentence1["clauses"][0]
    assert clause1["text"] == "She was happy", "First clause text should match."
    assert clause1["relationship"] is None, "First clause relationship should be None."
    assert "joy" in clause1["emotions"], "First clause should contain 'joy'."

    # Test the second paragraph
    paragraph2 = result["paragraphs"][1]
    assert paragraph2["id"] == 2, "Second paragraph ID should be 2."
    assert len(paragraph2["sentences"]) == 1, "Second paragraph should have one sentence."

    sentence2 = paragraph2["sentences"][0]
    assert sentence2["text"] == "The sun was shining brightly, and the birds were singing.", \
        "Second sentence text should match."