def is_rotation(str1, str2):
    return len(str1) == len(str2) and str2 in str1*2


def test_is_rotation():
    assert is_rotation("waterbottle", "erbottlewat")
    assert is_rotation("waterbottle", "rbottlewat") is False
