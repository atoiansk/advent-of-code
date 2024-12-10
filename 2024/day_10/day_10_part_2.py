from collections import deque
from utils import parse_input

def bfs(matrix, x, y):
    queue = deque()
    queue.append((x, y))
    score = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    previous_value = matrix[x][y]

    while queue:
        node = queue.popleft()
        x, y = node

        if matrix[x][y] == 9:
            score += 1

        previous_value = matrix[x][y]

        for direction in directions:
            dx, dy = direction
            current_x = x + dx
            current_y = y + dy

            if current_x < 0 or current_x >= len(matrix) or current_y < 0 or current_y >= len(matrix[0]):
                continue

            if matrix[current_x][current_y] != previous_value + 1:
                continue

            queue.append((current_x, current_y))

    return score

matrix = parse_input('input.txt')

total_score = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            total_score += bfs(matrix, i, j)

print(total_score)



