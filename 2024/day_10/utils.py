def parse_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    matrix = []
    for line in lines:
        matrix.append([int(char) for char in line.strip('\n')])

    return matrix
