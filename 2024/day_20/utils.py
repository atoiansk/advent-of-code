from collections import deque

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

def find_cheats(path, walls, end_position):
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cheats = {}
    initial_distance = path[end_position]

    for node in path:
        if node == end_position:
            continue

        for movement in movements:
            cheat_x = node[0] + movement[0]
            cheat_y = node[1] + movement[1]
            cheat_position = (cheat_x, cheat_y)

            # Check if cheating is possible
            if cheat_position in walls:
                for movement1 in movements:
                    cheat_x1 = cheat_x + movement1[0]
                    cheat_y1 = cheat_y + movement1[1]
                    cheat_position1 = (cheat_x1, cheat_y1)

                    if cheat_position1 in path:
                        cheat_distance = initial_distance + path[node] - path[cheat_position1] + 2

                        if cheat_distance < initial_distance:
                            start_position = node
                            end_position = cheat_position1
                            cheat = (start_position, end_position)
                            saving = initial_distance - cheat_distance

                            if cheat not in cheats:
                                cheats[cheat] = saving
                            else:
                                cheats[cheat] = max(cheats[cheat], saving)

    return cheats
