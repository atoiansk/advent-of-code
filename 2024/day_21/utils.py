import heapq

def find_path(start, end, keypad):
    movements = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }

    distances = {}
    pq = []

    distances[start] = 0

    # distance, node, path
    heapq.heappush(pq, (0, start, ''))

    shortest_paths = []

    while pq:
        distance, node, path = heapq.heappop(pq)

        if node == end:
            shortest_paths.append(path + 'A')
            continue

        if distances[node] < distance:
            continue

        for direction, movement in movements.items():
            next_node = (node[0] + movement[0], node[1] + movement[1])

            if next_node not in keypad.values():
                continue

            next_distance = distance + 1

            if next_node not in distances or next_distance <= distances[next_node]:
                distances[next_node] = next_distance
                heapq.heappush(pq, (next_distance, next_node, path + direction))

    return shortest_paths

def find_all_paths(keypad, combination):
    start = keypad['A']
    paths = set()
    paths.add('')
    for char in combination:
        end = keypad[char]
        new_paths = find_path(start, end, keypad)

        paths_copy = paths.copy()
        paths = set()
        for path in paths_copy:
            for new_path in new_paths:
                paths.add(path + new_path)

        start = end
    return paths

def get_complexity(combination, number_of_robots=3):
    door_key_pad = {
        'A': (2, 3),
        '0': (1, 3),
        '1': (0, 2),
        '2': (1, 2),
        '3': (2, 2),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '7': (0, 0),
        '8': (1, 0),
        '9': (2, 0)
    }

    robot_keypad = {
        'A': (2, 0),
        '<': (0, 1),
        '>': (2, 1),
        '^': (1, 0),
        'v': (1, 1)
    }

    current_paths = find_all_paths(door_key_pad, combination)
    minimum_length = min([len(x) for x in current_paths])

    for i in range(number_of_robots - 1):
        current_paths_copy = current_paths.copy()
        current_paths = set()

        for path in current_paths_copy:
            if len(path) == minimum_length:
                current_paths = current_paths | find_all_paths(robot_keypad, path)

        minimum_length = min([len(x) for x in current_paths])

    complexity = minimum_length * int(combination.strip('A'))

    return complexity
