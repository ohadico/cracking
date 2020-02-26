from itertools import zip_longest

from linkedlist import Node


def add(linked1, linked2):
    c = 0
    head = last = Node(0)
    for a, b in zip_longest(linked1, linked2, fillvalue=0):
        c += a + b
        last.next = Node(c % 10)
        c /= 10
    if c:
        last.next = Node(c)
    return head.next
