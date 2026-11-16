from dedup_lab.normalize import normalize


def test_lowercases():
    assert normalize("Hello World") == "hello world"
    assert normalize("HELLO WORLD") == "hello world"
    assert normalize("hElLo WoRlD") == "hello world"


def test_strip_whitespace():
    assert normalize("   Hello World   ") == "hello world"
    assert normalize("\tHello World\n") == "hello world"
    assert normalize("Hello   World") == "hello world"
    assert normalize("Hello \t \n  World") == "hello world"


def test_remove_special_characters():
    assert normalize("Hello, World!") == "hello world"
    assert normalize("Hello... World") == "hello world"
    assert normalize("Hello-World") == "hello world"
    assert normalize("Hello/World") == "hello world"
    assert normalize("Hello@World") == "hello world"
    assert normalize("Hello#World") == "hello world"
    assert normalize("Hello$World") == "hello world"
    assert normalize("Hello%World") == "hello world"
    assert normalize("Hello^World") == "hello world"
    assert normalize("Hello&World") == "hello world"
    assert normalize("Hello*World") == "hello world"
    assert normalize("Hello(World)") == "hello world"
    assert normalize("Hello[World]") == "hello world"
    assert normalize("Hello{World}") == "hello world"
    assert normalize("Hello|World") == "hello world"


def test_unicode_compatibility():
    assert normalize("Café") == "cafe"
    assert normalize("naïve") == "naive"
    assert normalize("résumé") == "resume"
    assert normalize("coöperate") == "cooperate"
    assert normalize("São Paulo") == "sao paulo"
    assert normalize("München") == "munchen"
    assert normalize("façade") == "facade"
    assert normalize("crème brûlée") == "creme brulee"


def test_idempotency():
    assert normalize("Hello World") == normalize(normalize("Hello World"))
    assert normalize("   Hello World   ") == normalize(normalize("   Hello World   "))
    assert normalize("Hello, World!") == normalize(normalize("Hello, World!"))
    assert normalize("Café") == normalize(normalize("Café"))
