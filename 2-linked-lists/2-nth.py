def nth(linked, n):
    buffer = [None] * n
    for i in linked:
        buffer.pop(0)
        buffer.append(i)
    return buffer.pop(0)
