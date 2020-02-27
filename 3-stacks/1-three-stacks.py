import random
from typing import Tuple

import pytest


class StackOnArr(object):
    def __init__(self, arr, tops, top_index, step, bounds):
        self._arr = arr
        self._tops = tops
        self._top_index = top_index
        self._step = step
        self.bounds = bounds

    def top(self):
        return self._tops[self._top_index]

    def push(self, v):
        if self._step > 0 and self.top() > min(self._tops[i] for i in self.bounds) or \
           self._step < 0 and self.top() < max(self._tops[i] for i in self.bounds):
            raise MemoryError()
        self._arr[self.top()] = v
        self._tops[self._top_index] += self._step

    def pop(self):
        self._tops[self._top_index] -= self._step
        if self.top() < 0 or self.top() >= len(self._arr):
            raise IndexError()
        v = self._arr[self.top()]
        # self._arr[self.top()] = None
        return v


def get_3_stacks(arr) -> Tuple[StackOnArr, StackOnArr, StackOnArr]:
    tops = [0, 1, len(arr) - 1]
    stack1 = StackOnArr(arr, tops, 0, 2, [2])
    stack2 = StackOnArr(arr, tops, 1, 2, [2])
    stack3 = StackOnArr(arr, tops, 2, -1, [0, 1])
    return stack1, stack2, stack3


def test_simple():
    array = [None] * 3
    s1, s3, s2 = get_3_stacks(array)
    s1.push(1)
    s2.push(2)
    s3.push(3)
    assert s1.pop() == 1
    assert s2.pop() == 2
    assert s3.pop() == 3


def test_reuse():
    array = [None] * 2
    s1, s2, s3 = get_3_stacks(array)
    s1.push(1)
    s2.push(2)
    assert s1.pop() == 1
    assert s2.pop() == 2
    s3.push(3)
    assert s3.pop() == 3


@pytest.mark.parametrize(('array',),
                         [([],),
                          ([None] * 3,)])
def test_empty(array):
    for s in get_3_stacks(array):
        with pytest.raises(IndexError):
            s.pop()


def test_full():
    for s in get_3_stacks([]):
        with pytest.raises(MemoryError):
            s.push(0)


@pytest.mark.parametrize(('n',),
                         [(1,),
                          (100,)])
def test_stacks(n):
    array = [None] * (2*n + 1)  # worst space consumption
    stacks = get_3_stacks(array)
    order = []
    for num in range(n):
        i = random.randint(0, len(stacks)-1)
        order.append(i)
        stacks[i].push(num)
    assert [stacks[i].pop() for i in reversed(order)][::-1] == list(range(n))
