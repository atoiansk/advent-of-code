def get_input():
    file = open('input.txt', 'r')
    lines = file.readlines()

    matrix = []
    for line in lines:
        matrix.append([char for char in line.strip('\n')])

    return matrix


def word_search(grid, x, y):
    if grid[x][y] != 'A':
        return False

    if x == 0 or x + 1 >= len(grid):
        return False

    if y == 0 or y + 1 >= len(grid[0]):
        return False

    first_diagonal = ''
    second_diagonal = ''

    first_diagonal += grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
    second_diagonal += grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]

    if (first_diagonal == 'MAS' or first_diagonal == 'SAM')  and (second_diagonal == 'MAS' or second_diagonal == 'SAM'):
        return True

    return False

final_count = 0

for x in range(len(get_input())):
    for y in range(len(get_input()[0])):
        final_count += word_search(get_input(), x, y)

print(final_count)

