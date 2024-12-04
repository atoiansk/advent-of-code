from collections import deque
import numpy as np

def get_input():
    file = open('input.txt', 'r')
    lines = file.readlines()

    matrix = []
    for line in lines:
        matrix.append([char for char in line.strip('\n')])

    return matrix


def word_search(grid, x, y, word):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    if grid[x][y] != word[0]:
        return count

    for direction in directions:
        dx, dy = direction
        k = 1

        current_x = x + dx
        current_y = y + dy

        while k < len(word):
            if current_x < 0 or current_x >= len(grid):
                break;

            if current_y < 0 or current_y >= len(grid[0]):
                break;

            if grid[current_x][current_y] != word[k]:
                break;

            k += 1
            current_x += dx
            current_y += dy

        if k == len(word):
            count += 1

    return count

final_count = 0

for x in range(len(get_input())):
    for y in range(len(get_input()[0])):
        final_count += word_search(get_input(), x, y, "XMAS")

print(final_count)

