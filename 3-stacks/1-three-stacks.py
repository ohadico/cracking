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
        if self._step > 0 and self.top() >= min(self._tops[i] for i in self.bounds) or \
           self._step < 0 and self.top() <= max(self._tops[i] for i in self.bounds):
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


def get_3_stacks(arr):
    tops = [0, 1, len(arr) - 1]
    stack1 = StackOnArr(arr, tops, 0, 2, [2])
    stack2 = StackOnArr(arr, tops, 1, 2, [2])
    stack3 = StackOnArr(arr, tops, 2, -1, [0, 1])
    return stack1, stack2, stack3
