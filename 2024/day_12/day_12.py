from collections import deque
from utils import parse_input, get_cost

def bfs(map, x, y):
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_plant = map[x][y]
    perimeter = 0
    area = 1

    while queue:
        node = queue.popleft()
        x, y = node

        for direction in directions:
            dx, dy = direction
            next_x = x + dx
            next_y = y + dy

            if next_x < 0 or next_x >= len(map) or next_y < 0 or next_y >= len(map[0]):
                perimeter += 1
                continue

            if map[next_x][next_y] != current_plant:
                perimeter += 1
                continue

            if (next_x, next_y) in visited:
                continue

            visited.add((next_x, next_y))
            queue.append((next_x, next_y))
            area += 1

    return perimeter, area, visited

map = parse_input('input.txt')
cost = get_cost(map, bfs)

print(cost)



