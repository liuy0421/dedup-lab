import re
import string
import unicodedata

_WHITESPACE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """
    Normalize text by removing accents and punctuations,
    handling whitespaces, and converting to lowercase.
    """
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation), ""))
    text = _WHITESPACE.sub(" ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.lower().strip()
