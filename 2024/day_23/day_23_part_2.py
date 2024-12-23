import itertools
from utils import parse_input

def validate_group(group, routes):
    pairs = list(itertools.combinations(group, 2))

    for pair in pairs:
        pair1, pair2 = pair
        if pair2 not in routes[pair1]:
            return False
    return True

def find_max_group(route, routes):
    for i in reversed(range(2, len(route))):
        groups = list(itertools.combinations(route, i))
        for group in groups:
            if validate_group(group, routes):
                return group
    return []

routes = parse_input("input.txt")

valid_routes = set()

for key, route in routes.items():
    for i in reversed(range(2, len(route))):
        groups = list(itertools.combinations(route, i))
        for group in groups:
            if validate_group(group, routes):
                new_group = group + (key,)
                group_list = list(new_group)
                group_list.sort()
                valid_routes.add(','.join(group_list))

max_length = 0
max_length_route = ""
for route in valid_routes:
    if len(route) > max_length:
        max_length = len(route)
        max_length_route = route

print(max_length_route)


