import spacy
import re

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')


def is_list(sentence):
    doc = nlp(sentence)
    lists = []
    current_list = []

    for token in doc:
        # If token is a comma or coordinating conjunction, continue processing
        if token.text == ',' or token.dep_ == 'cc':
            continue
        elif token.dep_ == 'conj':  # Conjunctive items
            # Ensure the conjunct is not part of a clause
            if token.head.pos_ in {'NOUN', 'ADJ', 'PROPN'}:
                current_list.append(token)
        elif token.pos_ in {'NOUN', 'ADJ', 'PROPN'}:  # Likely list item
            current_list.append(token)
        else:
            # Finalize the list if encountering a non-list token
            if len(current_list) > 1:
                lists.append(' '.join([t.text for t in current_list]))
            current_list = []

    # Handle any remaining list
    if len(current_list) > 1:
        lists.append(' '.join([t.text for t in current_list]))

    if lists:
        return True

def split_into_clauses_with_relationships(sentence):
    # Normalize spaces before splitting
    sentence = re.sub(r'\s+', ' ', sentence).strip()
    #print(sentence)
    #print(is_list(sentence))

    # Check if the sentence is a list (i.e., contains conjunctions like "and", "or")
    if is_list(sentence):
        # Treat the entire sentence as one clause (no relationship)
        return [{"text": sentence, "relationship": None}]

    # Step 1: Handle commas and FANBOYS conjunctions
    conjunction_split = re.split(r'(?:,)?( for | and | nor | but | or | yet | so )', sentence, flags=re.IGNORECASE)

    final_clauses = []
    previous_relationship = None
    previous_conjunction = None

    # Step 2: Process the split result
    #print(conjunction_split)
    for i in range(0, len(conjunction_split), 2):
        if previous_conjunction is not None:
            clause = previous_conjunction + ' ' + conjunction_split[i].strip()
        else: clause = conjunction_split[i].strip()

        # Attach the previous relationship to the current clause
        final_clauses.append({
            "text": clause,
            "relationship": previous_relationship
        })

        # Step 3: Determine the relationship for the next clause based on the conjunction
        if i + 1 < len(conjunction_split):
            conjunction = conjunction_split[i + 1].strip().lower()

            # Handle relationship based on conjunction
            if ("but" or "yet") in conjunction:
                previous_relationship = "contrast"
            elif ("and" or "so") in conjunction:
                previous_relationship = "reinforcement"
            else:
                previous_relationship = None
            previous_conjunction = conjunction



    return final_clauses


def segment_text(text):
    paragraphs = text.split("\n\n")  # Split into paragraphs
    segmented = []
    for i, paragraph in enumerate(paragraphs, start=1):
        cleaned_paragraph = re.sub(r'\s+', ' ', paragraph).strip()
        doc = nlp(cleaned_paragraph)
        sentences = []
        for sent in doc.sents:
            # Split sentence into clauses with relationships
            clauses = split_into_clauses_with_relationships(sent.text)
            sentences.append({
                "text": sent.text,
                "clauses": clauses
            })
        if sentences:
            segmented.append({
                "paragraph": i,
                "sentences": sentences
            })
    return segmented



