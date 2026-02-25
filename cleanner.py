import re

def clean_text(text):
    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove very short lines (like menu items)
    sentences = text.split(". ")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 40]

    # Remove duplicates
    unique_sentences = list(dict.fromkeys(sentences))

    return ". ".join(unique_sentences)