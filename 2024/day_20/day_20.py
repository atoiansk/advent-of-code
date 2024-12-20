from utils import parse_input, find_cheats

walls, start_position, end_position = parse_input("input.txt")

def over_100(cheats):
    over_100 = 0
    for cheat in cheats.values():
        if cheat >= 100:
            over_100 += 1
    return over_100

# Part 1
cheats = find_cheats(walls, start_position, end_position, 2)

print(over_100(cheats))

# Part 2
cheats = find_cheats(walls, start_position, end_position, 20)

print(over_100(cheats))
