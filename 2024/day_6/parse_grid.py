import guard

def parse_grid(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    grid = []
    start_position = None
    start_direction = None

    for i in range(len(lines)):
        grid.append([])
        line = lines[i].strip('\n')
        for char in line:
            if char in guard.Guard.directions:
                start_position = (i, line.index(char))
                start_direction = char
            grid[i].append(char)

    return grid, start_position, start_direction
