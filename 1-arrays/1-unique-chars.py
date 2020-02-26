import pytest


# space: O(n), time: O(n)
def is_unique(string):
    return len(string) == len(set(string))


# space: O(1), time: O(n^2)
def is_unique2(string):
    if len(string) < 2:
        return True
    return all(string[i] != string[j] for i in range(len(string) - 1) for j in range(i + 1, len(string)))


# space: O(1), time: O(n)
def is_unique3(string):
    characters = [0] * 256
    for c in string:
        characters[ord(c)] += 1
    return all(n < 2 for n in characters)


@pytest.mark.parametrize("func", (is_unique, is_unique2, is_unique3))
def test_is_unique(func):
    assert func("Hello") is False
    assert func("World") is True
