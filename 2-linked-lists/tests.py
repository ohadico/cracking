from linkedlist import linkedlist


def test_linkedlist():
    assert list(linkedlist(range(10))) == list(range(10))
