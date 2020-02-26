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
