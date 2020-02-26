import pytest


def reverse(string):
    l = len(string)
    for i in range(l // 2):
        temp = string[i]
        string[i] = string[l - i - 1]
        string[l - i - 1] = temp
    return string


@pytest.mark.parametrize("string", ("abcde", "abcba", "abba"))
def test_reverse(string):
    assert reverse(list(string)) == list(reversed(string))
