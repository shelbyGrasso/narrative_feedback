from src.text_processor import segment_text, is_list, split_into_clauses_with_relationships

# Tests for segmenting text into sentences

def test_split_into_clauses():
    sentence = "She was happy, but she felt nervous."
    clauses = split_into_clauses_with_relationships(sentence)
    assert len(clauses) == 2
    assert clauses[0]["text"] == "She was happy"
    assert clauses[1]["relationship"] == "contrast"

def test_segment_text():
    text = "He smiled and walked away. But he was sad."
    result = segment_text(text)
    assert len(result[0]["sentences"]) == 2

# Test: Simple case with two sentences
def test_segment_text_simple_case():
    text = "This is the first sentence. This is the second sentence."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "This is the first sentence.",
                    "clauses": [{"text": "This is the first sentence.", "relationship": None}]
                },
                {
                    "text": "This is the second sentence.",
                    "clauses": [{"text": "This is the second sentence.", "relationship": None}]
                }
            ]
        }
    ]

# Test: Empty input
def test_segment_text_empty_string():
    text = ""
    result = segment_text(text)
    assert result == []

# Test: Single sentence without punctuation
def test_segment_text_no_punctuation():
    text = "This is a single sentence without punctuation"
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "This is a single sentence without punctuation",
                    "clauses": [{"text": "This is a single sentence without punctuation", "relationship": None}]
                }
            ]
        }
    ]

# Test: Sentences with mixed punctuation
def test_segment_text_mixed_punctuation():
    text = "Hello! How are you? I am fine."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "Hello!",
                    "clauses": [{"text": "Hello!", "relationship": None}]
                },
                {
                    "text": "How are you?",
                    "clauses": [{"text": "How are you?", "relationship": None}]
                },
                {
                    "text": "I am fine.",
                    "clauses": [{"text": "I am fine.", "relationship": None}]
                }
            ]
        }
    ]

# Test: Extra spaces between sentences
def test_segment_text_extra_spaces():
    text = "This is the first sentence.    This is the second sentence."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "This is the first sentence.",
                    "clauses": [{"text": "This is the first sentence.", "relationship": None}]
                },
                {
                    "text": "This is the second sentence.",
                    "clauses": [{"text": "This is the second sentence.", "relationship": None}]
                }
            ]
        }
    ]

# Test: Handles newline characters
def test_segment_text_with_newlines():
    text = "This is the first sentence.\nThis is the second sentence."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "This is the first sentence.",
                    "clauses": [{"text": "This is the first sentence.", "relationship": None}]
                },
                {
                    "text": "This is the second sentence.",
                    "clauses": [{"text": "This is the second sentence.", "relationship": None}]
                }
            ]
        }
    ]

def test_segment_text_with_abbreviations():
    text = "Dr. Smith is here. He arrived at 10 a.m."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "Dr. Smith is here.",
                    "clauses": [{"text": "Dr. Smith is here.", "relationship": None}]
                },
                {
                    "text": "He arrived at 10 a.m.",
                    "clauses": [{"text": "He arrived at 10 a.m.", "relationship": None}]
                }
            ]
        }
    ]

def test_segment_text_with_paragraph_metadata():
    text = (
        "This is the first sentence of paragraph one.\n\n"
        "This is the first sentence of paragraph two. This is the second sentence of paragraph two."
    )
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "This is the first sentence of paragraph one.",
                    "clauses": [{"text": "This is the first sentence of paragraph one.", "relationship": None}]
                }
            ]
        },
        {
            "paragraph": 2,
            "sentences": [
                {
                    "text": "This is the first sentence of paragraph two.",
                    "clauses": [{"text": "This is the first sentence of paragraph two.", "relationship": None}]
                },
                {
                    "text": "This is the second sentence of paragraph two.",
                    "clauses": [{"text": "This is the second sentence of paragraph two.", "relationship": None}]
                }
            ]
        }
    ]

def test_segment_text_with_contrasting_clauses():
    text = "I’m sad, but I’m also hopeful."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "I’m sad, but I’m also hopeful.",
                    "clauses": [
                        {"text": "I’m sad", "relationship": None},
                        {"text": "but I’m also hopeful.", "relationship": "contrast"}
                    ]
                }
            ]
        }
    ]

def test_segment_text_with_reinforcing_clauses():
    text = "I’m happy, and I'm grateful."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "I’m happy, and I'm grateful.",
                    "clauses": [
                        {"text": "I’m happy", "relationship": None},
                        {"text": "and I'm grateful.", "relationship": "reinforcement"}
                    ]
                }
            ]
        }
    ]

def test_segment_text_with_mixed_clauses():
    text = "I’m tired, but I’m determined, and I’ll keep going."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "I’m tired, but I’m determined, and I’ll keep going.",
                    "clauses": [
                        {"text": "I’m tired", "relationship": None},
                        {"text": "but I’m determined", "relationship": "contrast"},
                        {"text": "and I’ll keep going.", "relationship": "reinforcement"}
                    ]
                }
            ]
        }
    ]

def test_is_list_with_and():
    text = "I bought apples, oranges, and bananas."
    result = is_list(text)
    assert result == True  # Should detect this as a list

def test_segment_text_with_list():
    text = "I bought apples, oranges, and bananas."
    result = segment_text(text)
    assert result == [
        {
            "paragraph": 1,
            "sentences": [
                {
                    "text": "I bought apples, oranges, and bananas.",
                    "clauses": [{"text": "I bought apples, oranges, and bananas.", "relationship": None}]
                }
            ]
        }
    ]
