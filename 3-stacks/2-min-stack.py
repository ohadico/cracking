from typing import Tuple, List


def push(stack: Tuple[List, List[Tuple]], new_val):
    stack[0].append(new_val)
    if stack[1]:
        last_min = stack[1][-1]
        if new_val < last_min[0]:
            stack[1].append((new_val, 1))
        elif new_val == last_min[0]:
            stack[1][-1] = (last_min[0], last_min[1]+1)
    else:
        stack[1].append((new_val, 1))


def pop(stack):
    val = stack[0].pop()
    last_min = stack[1][-1]
    if val == last_min[0]:
        if last_min[1] == 1:
            stack[1].pop()
        else:
            stack[1][-1] = (last_min[0], last_min[1]-1)
    return val


def get_min(stack):
    if stack[1]:
        return stack[1][-1][0]


def test_min_stack():
    stack = ([], [])
    for i in (3, 1, 2, 0):
        push(stack, i)

    assert get_min(stack) == 0
    pop(stack)
    assert get_min(stack) == 1
    pop(stack)
    pop(stack)
    pop(stack)
