import math


def push(stack, new_val):
    stack.append((new_val, get_min(stack)))


def pop(stack):
    return stack.pop()[0]


def get_min(stack):
    if stack:
        return min(stack[-1])
    return math.inf


def test_min_stack():
    stack = []
    for i in (3, 1, 2, 0):
        push(stack, i)

    assert get_min(stack) == 0
    stack.pop()
    assert get_min(stack) == 1
    stack.pop()
    stack.pop()
    stack.pop()
