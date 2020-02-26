def remove_dups(string):
    dups = [False] * 256
    write = 0
    for c in string:
        if dups[ord(c)]:
            continue
        string[write] = c
        write += 1
    return string[:write]


def test_remove_dups():
    assert remove_dups(list("")) == ""
    assert remove_dups(list("aaaabbbcc")) == "abc"
    assert remove_dups(list("Hello, World!")) == "Helo, World!"
