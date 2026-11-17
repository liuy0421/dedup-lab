import pytest

from dedup_lab.normalize import normalize

CASES = [
    # case + whitespace
    ("Hello World", "hello world"),
    ("hElLo WoRlD", "hello world"),
    ("   Hello World   ", "hello world"),
    ("Hello \t \n  World", "hello world"),
    ("Hello\u00a0World", "hello world"),  # non-breaking space
    ("Hel\u200blo World", "hello world"),  # zero-width space (invisible!)
    ("Straße", "strasse"),  # needs casefold(), not lower()
    # ASCII punctuation (category P)
    ("Hello, World!", "hello world"),
    ("Hello... World", "hello world"),
    ("Hello-World", "hello world"),
    ("Hello(World)", "hello world"),
    # symbols (category S): decided to strip these too
    ("Hello$World", "hello world"),
    ("Hello|World", "hello world"),
    ("2+2=4", "2 2 4"),  # documents the math trade-off
    # non-ASCII punctuation
    ("“Hello” — World", "hello world"),
    ("你好，世界。", "你好 世界"),
    # compatibility forms
    ("ＨＥＬＬＯ", "hello"),
    ("ﬁle", "file"),
    # Latin accents stripped
    ("crème brûlée", "creme brulee"),
    ("São Paulo", "sao paulo"),
    # non-Latin preserved
    ("Привет мир", "привет мир"),
    ("안녕하세요 세계", "안녕하세요 세계"),
    ("がっこう", "がっこう"),  # dakuten must survive
    ("नमस्ते दुनिया", "नमस्ते दुनिया"),  # Devanagari vowel signs must survive
    ("مرحبا بالعالم", "مرحبا بالعالم"),
    # edge cases
    ("", ""),
    ("!!!", ""),
    ("Room 101", "room 101"),
]


@pytest.mark.parametrize(("raw", "expected"), CASES)
def test_normalize(raw, expected):
    assert normalize(raw) == expected


@pytest.mark.parametrize("raw", [raw for raw, _ in CASES])
def test_idempotent(raw):
    once = normalize(raw)
    assert normalize(once) == once
