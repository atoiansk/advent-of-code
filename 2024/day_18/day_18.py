import heapq
from utils import parse_input, dijskstra

# Test
bytes = parse_input("test_input.txt")
bytes_set = set(bytes[:12])

print(dijskstra(7, (0, 0), bytes_set, (6, 6)))

# Part 1
bytes = parse_input("input.txt")
bytes_set = set(bytes[:1024])

print(dijskstra(71, (0, 0), bytes[:1024], (70, 70)))

# Part 2 - Test
bytes = parse_input("test_input.txt")

for i in range(len(bytes)):
    bytes_set = set(bytes[:i])
    target_distance = dijskstra(7, (0, 0), bytes_set, (6, 6))
    if target_distance is None:
        print(bytes[i - 1])
        break

# Part 2
bytes = parse_input("input.txt")

for i in range(len(bytes)):
    bytes_set = set(bytes[:i])
    target_distance = dijskstra(71, (0, 0), bytes_set, (70, 70))
    if target_distance is None:
        print(bytes[i - 1])
        break


