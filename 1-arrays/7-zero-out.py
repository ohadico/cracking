def zero_out(mat):
    n = len(mat)
    rows = set()
    cols = set()
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(n):
        for j in range(n):
            if i in rows or j in cols:
                mat[i][j] = 0
    return mat


def test_zero_out():
    mat = [[1, 2, 3, 4],
           [0, 2, 3, 0],
           [1, 2, 3, 4],
           [0, 2, 3, 4]]
    res = [[0, 2, 3, 0],
           [0, 0, 0, 0],
           [0, 2, 3, 0],
           [0, 0, 0, 0]]
    assert zero_out([]) == []
    assert zero_out([[0]]) == [[0]]
    assert zero_out(mat) == res
