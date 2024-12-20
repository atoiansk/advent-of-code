from collections import deque
from time import sleep
def parse_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    start_position = None
    end_position = None
    walls = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                walls.add((j,i))
            elif lines[i][j] == "S":
                start_position = (j,i)
            elif lines[i][j] == "E":
                end_position = (j,i)

    return walls, start_position, end_position

def dfs(walls, start_position, end_position):
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = deque([(start_position, 0)])
    visited = {}
    visited[start_position] = 0

    while queue:
        current_position, current_distance = queue.popleft()

        for movement in movements:
            new_position = (current_position[0] + movement[0], current_position[1] + movement[1])

            if new_position in walls:
                continue

            if new_position in visited.keys():
                continue

            visited[new_position] = current_distance + 1
            queue.append((new_position, current_distance + 1))

    return visited

def find_cheats(walls, start_position, end_position, cheat_length):
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cheats = {}
    path = dfs(walls, start_position, end_position)
    initial_distance = path[end_position]
    max_x = max(walls, key=lambda x: x[0])[0]
    max_y = max(walls, key=lambda x: x[1])[1]

    for node in path:
        if node == end_position:
            continue

        start_positions = {node: 0}
        visited = set()

        while start_positions:
            start_positions_copy = start_positions.copy()
            start_positions = {}
            for start_position, moves in start_positions_copy.items():
                for movement1 in movements:
                    cheat_x1 = start_position[0] + movement1[0]
                    cheat_y1 = start_position[1] + movement1[1]
                    cheat_position1 = (cheat_x1, cheat_y1)

                    if cheat_position1 in visited:
                        continue

                    visited.add(cheat_position1)

                    if cheat_x1 < 0 or cheat_x1 > max_x or cheat_y1 < 0 or cheat_y1 > max_y:
                        continue

                    if moves + 1 < cheat_length:
                        start_positions[cheat_position1] = moves + 1

                    if cheat_position1 in path:
                        cheat_distance = initial_distance + path[node] - path[cheat_position1] + moves + 1

                        if cheat_distance < initial_distance:
                            cheat = (node, cheat_position1)
                            saving = initial_distance - cheat_distance

                            if cheat not in cheats:
                                cheats[cheat] = saving
                            else:
                                cheats[cheat] = max(cheats[cheat], saving)
    return cheats


