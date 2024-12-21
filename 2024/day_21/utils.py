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

    shortest_paths = set()

    while pq:
        distance, node, path = heapq.heappop(pq)

        if node == end:
            shortest_paths.add(path + 'A')
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

cache = {}

def find_minimal_length(start, end, times, keypad):
    robot_keypad = {
        'A': (2, 0),
        '<': (0, 1),
        '>': (2, 1),
        '^': (1, 0),
        'v': (1, 1)
    }

    if (start, end, times) in cache:
        return cache[(start, end, times)]

    paths = find_path(start, end, keypad)

    if times == 0:
        return min([len(x) for x in paths])

    minimal_length = 1<<60
    for path in paths:
        cost = 0
        current_start = robot_keypad['A']
        for char in path:
            current_end = robot_keypad[char]
            cost += find_minimal_length(current_start, current_end, times - 1, robot_keypad)
            current_start = current_end

        minimal_length = min(cost, minimal_length)

    cache[(start, end, times)] = minimal_length
    return minimal_length

def get_code_cost(code, times=2):
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

    start = door_key_pad['A']
    cost = 0
    for digit in code:
        end = door_key_pad[digit]
        char_cost = find_minimal_length(start, end, times, door_key_pad)
        cost += char_cost
        start = end
    return cost
