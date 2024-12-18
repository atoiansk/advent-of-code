import heapq

def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    return [tuple(map(int, line.split(","))) for line in lines]

def dijskstra(grid_size, start, bytes, end):
    distances = {}
    pq = []

    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distances[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        distance, position = heapq.heappop(pq)

        if distances[position] < distance:
            continue

        for movement in movements:
            new_x = position[0] + movement[0]
            new_y = position[1] + movement[1]

            new_position = (new_x, new_y)
            if new_x < 0 or new_x >= grid_size or new_y < 0 or new_y >= grid_size:
                continue

            if new_position in bytes:
                continue

            new_distance = distance + 1

            if new_position == end:
                return new_distance

            if new_position not in distances or distances[new_position] > new_distance:
                distances[new_position] = new_distance
                heapq.heappush(pq, (new_distance, new_position))

    return None
