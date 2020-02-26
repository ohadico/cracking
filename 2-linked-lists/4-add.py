from itertools import zip_longest

from linkedlist import Node, linkedlist


def add(linked1, linked2):
    c = 0
    head = last = Node(0)
    for a, b in zip_longest(linked1, linked2, fillvalue=0):
        c += a + b
        last.next = Node(c % 10)
        last = last.next
        c //= 10
    if c:
        last.next = Node(c)
    return head.next


def test_add():
    a = linkedlist((3, 1, 5))
    b = linkedlist((5, 9, 2))
    c = add(a, b)
    assert list(c) == [8, 0, 8]
