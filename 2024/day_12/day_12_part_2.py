from collections import deque
from utils import parse_input, get_cost

def bfs(map, x, y):
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    perimeter = 0

    current_plant = map[x][y]
    area = 1

    sides = {
        (0, 1): [],
        (0, -1): [],
        (1, 0): [],
        (-1, 0): []
    }

    while queue:
        node = queue.popleft()
        x, y = node

        for direction in directions:
            dx, dy = direction
            next_x = x + dx
            next_y = y + dy

            if next_x < 0 or next_x >= len(map) or next_y < 0 or next_y >= len(map[0]) or map[next_x][next_y] != current_plant:
                sides[direction].append((x, y, 1))
                continue

            if (next_x, next_y) in visited:
                continue

            visited.add((next_x, next_y))
            queue.append((next_x, next_y))
            area += 1

    perimeter = count_sides(sides)
    return perimeter, area, visited

def count_sides(sides):
    count = 0

    for direction, side_list in sides.items():
        # direction of movement
        _y, index = direction
        x = 0
        y = 1

        anti_index = int(not index)

        side_list = sorted(side_list, key=lambda x: x[anti_index])

        while x < len(side_list):
            while y < len(side_list):
                side = (side_list[x][0], side_list[x][1])
                length = side_list[x][2]
                compare_side = (side_list[y][0], side_list[y][1])

                if compare_side[index] != side[index]:
                    y += 1
                    continue

                if abs(compare_side[anti_index] - side[anti_index]) == length:
                    side_list.pop(y)

                    if index == 0:
                        side_list[x] = (side[0], min(side[1], compare_side[1]), length + 1)
                    else:
                        side_list[x] = (min(side[0], compare_side[0]), side[1], length + 1)
                    continue
                y += 1
            x += 1
            y = x + 1

        count += len(side_list)

    return count

map = parse_input('input.txt')
cost = get_cost(map, bfs)

print(cost)
