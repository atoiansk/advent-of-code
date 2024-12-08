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

    return antenas, m, n

def print_grid(m, n, antenas, antinodes):
    for i in range(m):
        for j in range(n):
            if any((i,j) in arr for arr in antenas.values()):
                matching_keys = [key for key, array in antenas.items() if (i,j) in array]
                print(matching_keys[0], end='')
            elif (i,j) in antinodes:
                print('#', end='')
            else:
                print('.', end='')
        print()

def out_of_bounds(node, m, n):
    if node[0] < 0 or node[1] < 0:
        return True

    if node[0] >= m or node[1] >= n:
        return True

    return False

def find_keys_with_element(dictionary, element):
     return [key for key, array in dictionary.items() if element in array]
