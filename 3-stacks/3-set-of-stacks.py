

N = 3


def push(set_of_stacks, val):
    if len(set_of_stacks) == 0 or len(set_of_stacks[-1]) == 0:
        set_of_stacks.append([])
    set_of_stacks[-1].append(val)


def pop(set_of_stacks, index=-1):
    val = set_of_stacks[index].pop()
    if set_of_stacks and len(set_of_stacks[-1]) == 0:
        set_of_stacks.pop()
    return val


def test_set_of_stacks():
    set_of_stacks = []
    for i in range(10):
        push(set_of_stacks, i)

    for i in range(9, -1, -1):
        assert pop(set_of_stacks) == i
