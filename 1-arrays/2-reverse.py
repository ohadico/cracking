import pytest


def reverse(string):
    l = len(string)
    for i in range(l // 2):
        temp = string[i]
        string[i] = string[l - i]
        string[l - i] = temp
    return string


@pytest.mark.parametrize("string", ("abcde", "abcba", "abba"))
def test_reverse(string):
    assert reverse(string) == reversed(string)
