import heapq
import sys

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

def dijkstra(walls, start_position):
    # 0 = north, 1 = east, 2 = south, 3 = west
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    heading = 1 # start facing east

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

walls, start_position, end_position = parse_input('input.txt')

distances = dijkstra(walls, start_position)
minimum_distance = sys.maxsize

for h in range(4):
    minimum_distance = min(minimum_distance, distances[(end_position, h)])

print(minimum_distance)
