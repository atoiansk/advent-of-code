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

max_route_length = 0
longest_route = None

for key, route in routes.items():
    max_group = find_max_group(route, routes)
    max_group += (key,)
    group_list = list(max_group)
    if len(group_list) > max_route_length:
        max_route_length = len(group_list)
        longest_route = group_list

longest_route.sort()
print(','.join(longest_route))


