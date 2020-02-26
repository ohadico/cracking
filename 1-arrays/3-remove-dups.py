import pytest


def remove_dups(string):
    dups = [False] * 256
    write = 0
    for c in string:
        if dups[ord(c)]:
            continue
        string[write] = c
        write += 1
        dups[ord(c)] = True
    return string[:write]


@pytest.mark.parametrize(("before", "after"),
                         [("", ""),
                          ("aaaabbbcc", "abc"),
                          ("Hello, World!", "Helo, Wrd!")])
def test_remove_dups(before, after):
    assert remove_dups(list(before)) == list(after)
