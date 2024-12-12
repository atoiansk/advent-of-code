def parse_input(filename):
    file = open(filename, 'r')
    map = []

    for line in file.readlines():
        map.append([char for char in line.strip('\n')])

    return map

def get_cost(map, bfs):
    total_visited = set()
    cost = 0

    for x in range(len(map)):
        for y in range(len(map[x])):
            if (x, y) in total_visited:
                continue

            perimeter, area, visited = bfs(map, x, y)
            cost += perimeter * area
            total_visited = total_visited | visited

    return cost

