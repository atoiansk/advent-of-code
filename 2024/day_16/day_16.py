from utils import parse_input, dijkstra, get_optimal_nodes, print_grid
import sys

walls, start_position, end_position = parse_input('input.txt')

distances = dijkstra(walls, start_position)
minimum_distance = sys.maxsize
minimum_distance_position = None

for h in range(4):
    if distances[(end_position, h)] < minimum_distance:
        minimum_distance = distances[(end_position, h)]
        minimum_distance_position = (end_position, h)

# Part 1
print("Part 1")
print(minimum_distance)

#Part 2
print("Part 2")

from_start = distances

optimum_end_postion, optimum_end_heading = minimum_distance_position
flipped_heading = (optimum_end_heading + 2) % 4

from_end = dijkstra(walls, optimum_end_postion, flipped_heading)

nodes = get_optimal_nodes(end_position, optimum_end_heading, from_start, from_end, minimum_distance)

print(len(nodes))
