from utils import parse_input, dfs, find_cheats

walls, start_position, end_position = parse_input("input.txt")

path = dfs(walls, start_position, end_position)

cheats = find_cheats(path, walls, end_position)

# Part 1
over_100 = 0

for cheat in cheats.values():
    if cheat >= 100:
        over_100 += 1

print(over_100)
