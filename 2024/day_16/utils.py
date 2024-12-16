import heapq, sys
from collections import deque

def parse_input(file_name):
    file = open(file_name, 'r')

    walls = set()
    start_position = None
    end_position = None

    for i, line in enumerate(file):
        for j, char in enumerate(line):
            if char == '#':
                walls.add((j, i))
            elif char == 'S':
                start_position = (j, i)
            elif char == 'E':
                end_position = (j, i)

    return walls, start_position, end_position

def dijkstra(walls, start_position, start_heading = 1):
    # 0 = north, 1 = east, 2 = south, 3 = west
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    heading = start_heading

    distances = {}
    pq = []

    distances[(start_position, heading)] = 0
    heapq.heappush(pq, (0, start_position, heading))

    while pq:
        distance, position, heading = heapq.heappop(pq)

        if distances[(position, heading)] < distance:
            continue

        # Handle turns
        for movement in movements:
            next_heading = movements.index(movement)

            # Skip if it's the same heading
            if next_heading == heading:
                continue

            # Skip if it's a 180 degree turn
            if abs(next_heading - heading) == 2:
                continue

            new_distance = distance + 1000
            if (position, next_heading) not in distances or distances[(position, next_heading)] > new_distance + 1000:
                distances[(position, next_heading)] = new_distance
                heapq.heappush(pq, (new_distance, position, next_heading))

        # Handle moving forward
        dx, dy = movements[heading]
        next_position = (position[0] + dx, position[1] + dy)

        if next_position in walls:
            continue

        new_distance = distance + 1

        if (next_position, heading) not in distances or distances[(next_position, heading)] > new_distance:
            distances[(next_position, heading)] = new_distance
            heapq.heappush(pq, (new_distance, next_position, heading))

    return distances

def get_optimal_nodes(start_position, start_heading, from_start, from_end, optimum_distance):
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    heading = start_heading

    nodes = set()

    queue = deque()
    queue.append((start_position, start_heading))

    while queue:
        position, heading = queue.popleft()
        nodes.add(position)

        flipped_heading = (heading + 2) % 4

        next_x = position[0] + movements[flipped_heading][0]
        next_y = position[1] + movements[flipped_heading][1]

        next_position = (next_x, next_y)

        for i in range(4):
            state_from_start = (next_position, i)
            state_from_end = (next_position, (i + 2) % 4)

            # Check if node distance from start plus node distance from end equals the optimum distance
            if state_from_start in from_start and state_from_end in from_end:
                if from_start[state_from_start] + from_end[state_from_end] == optimum_distance:
                    queue.append((next_position, i))

    return nodes

def print_grid(walls, nodes):
    x = max(walls, key=lambda x: x[0])[0]
    y = max(walls, key=lambda x: x[1])[1]

    for i in range(y + 1):
        for j in range(x + 1):
            if (j, i) in walls:
                print("#", end="")
            elif (j, i) in nodes:
                print("O", end="")
            else:
                print(".", end="")
        print()


