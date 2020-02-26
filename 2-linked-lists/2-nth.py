import pytest

from linkedlist import linkedlist


def nth(linked, n):
    buffer = [None] * n
    for i in linked:
        buffer.pop(0)
        buffer.append(i)
    return buffer.pop(0)


@pytest.mark.parametrize(("end", 'n'),
                         [(10, 1),
                          (10, 3),
                          (10, 10),
                          (10, 12)])
def test_nth(end, n):
    seq = range(1, end + 1)
    head = linkedlist(seq)
    assert nth(head, n) == (seq[-n] if n <= end else None)
