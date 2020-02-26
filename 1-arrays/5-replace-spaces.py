def replace_spaces(string):
    buffer = []
    read = write = 0
    l = len(string)
    while i < l:
        buffer.append(string[i]); i += 1
        c = buffer.pop(0)
        if c != ' ':
            string[write] = c if write < l else string.append(c); write += 1
            continue
        buffer.append(string[i]); i += 1
        buffer.append(string[i]); i += 1
        string[write] = '%' if write < l else string.append('%'); write += 1
        string[write] = '2' if write < l else string.append('2'); write += 1
        string[write] = '0' if write < l else string.append('0'); write += 1
