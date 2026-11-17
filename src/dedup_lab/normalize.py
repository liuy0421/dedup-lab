import re
import sys
import unicodedata

_WHITESPACE = re.compile(r"\s+")


def _build_table() -> dict[int, str | None]:
    table: dict[int, str | None] = {}
    for cp in range(sys.maxunicode + 1):  # every code point, ~1.1M
        cat = unicodedata.category(chr(cp))
        if cat == "Cf":
            table[cp] = None  # None = delete
        elif cat[0] in "PS":
            table[cp] = " "  # punctuation/symbol → space
    return table


_PUNCT_SYMBOL_FORMAT = _build_table()  # runs once, ~0.5 s at import


def _is_latin(ch: str) -> bool:
    return unicodedata.name(ch, "").startswith("LATIN")


def _strip_latin_accents(text: str) -> str:
    """
    Remove combining marks only when they follow a Latin base letter.
    This preserves marks on non-Latin scripts (e.g., Japanese, Hindi)."""
    out = []
    prev_base_is_latin = False
    for ch in unicodedata.normalize("NFD", text):
        if unicodedata.category(ch).startswith("M"):
            if not prev_base_is_latin:
                out.append(ch)  # keep marks on Japanese, Hindi, etc.
        else:
            out.append(ch)
            prev_base_is_latin = _is_latin(ch)
    return unicodedata.normalize("NFC", "".join(out))


def normalize(text: str) -> str:
    """
    Normalize text by removing accents and punctuations,
    handling whitespaces, and converting to lowercase.
    """
    text = unicodedata.normalize("NFKC", text)
    text = _strip_latin_accents(text)
    text = unicodedata.normalize("NFC", text)
    text = text.translate(_PUNCT_SYMBOL_FORMAT)
    text = _WHITESPACE.sub(" ", text)
    return text.casefold().strip()
