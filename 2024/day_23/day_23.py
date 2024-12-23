import itertools
from utils import parse_input

routes = parse_input("input.txt")

three_way_routes = set()

for key, route in routes.items():
    pairs = list(itertools.combinations(route, 2))

    for pair in pairs:
        pair1, pair2 = pair
        if pair2 in routes[pair1]:
            elements = [key, pair1, pair2]
            elements.sort()
            three_way_routes.add(','.join(elements))

total_wit_t = 0

for route in three_way_routes:
    if ',t' in route or route[0] == 't':
        total_wit_t += 1

print(total_wit_t)
