from typing import Optional


class Node(object):
    def __init__(self, val, next: Optional['Node'] = None):
        self.val = val
        self.next = next

    def __next__(self):
        return self.next

    def __iter__(self):
        c = self
        while c:
            yield c.val
            c = next(c)

    def __str__(self):
        return "({}, {})".format(self.val, "->" if self.next else '-')


def linkedlist(it):
    prev = None
    for i in reversed(it):
        prev = Node(i, prev)
    return prev
