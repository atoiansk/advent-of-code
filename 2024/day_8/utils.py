def parse_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()

    m = len(lines)
    n = len(lines[0].strip('\n'))
    antenas = {}

    for i in range(m):
        for j in range(n):
            if lines[i][j] != '.':
                antenas.setdefault(lines[i][j], []).append((i, j))

    return m, n, antenas
