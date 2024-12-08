from utils import parse_input
from map import Map

m, n, antenas = parse_input('input.txt')

map = Map(m, n, antenas)

map.print_grid()

# print(map.get_antinodes())

print(len(map.get_antinodes(True)))

