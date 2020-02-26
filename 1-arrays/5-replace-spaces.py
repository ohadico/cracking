import pytest


def write_or_append(string, index, c, length):
    if index < length:
        string[index] = c
    else:
        string.append(c)


def replace_spaces(string):
    buffer = []
    i = write = 0
    l = len(string)
    if i < l:
        buffer.append(string[i]); i += 1
    while buffer:
        if i < l:
            buffer.append(string[i]); i += 1
        c = buffer.pop(0)
        if c != ' ':
            write_or_append(string, write, c, l); write += 1
            continue
        if i < l:
            buffer.append(string[i]); i += 1
        if i < l:
            buffer.append(string[i]); i += 1
        write_or_append(string, write, '%', l); write += 1
        write_or_append(string, write, '2', l); write += 1
        write_or_append(string, write, '0', l); write += 1

    return string


@pytest.mark.parametrize(("string",), [("",),
                                       ("a b",),
                                       (" Hello , World ! ",)])
def test_replace_spaces(string: str):
    assert ''.join(replace_spaces(list(string))) == string.replace(' ', "%20")
