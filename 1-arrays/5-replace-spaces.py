import pytest


def write_or_append(string, index, c, length):
    if index < length:
        string[index] = c
    else:
        string.append(c)


# space: O(n), time: O(n)
def replace_spaces(string):
    replaced = ""
    for c in string:
        replaced += c if c != ' ' else "%20"
    return replaced


@pytest.mark.parametrize(("string",), [("",),
                                       ("a b",),
                                       (" Hello , World ! ",)])
def test_replace_spaces(string: str):
    assert ''.join(replace_spaces(list(string))) == string.replace(' ', "%20")
