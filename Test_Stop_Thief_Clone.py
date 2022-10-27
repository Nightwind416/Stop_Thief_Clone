from Stop_Thief_Clone import main



def test_lowercase():
    assert shorten("hello world") == "hll wrld"


def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_numbers():
    assert shorten("42") == "42"


def test_punctuation():
    assert shorten(" # @ ! . ; ' ") == " # @ ! . ; ' "