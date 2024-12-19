def parse_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    patterns = set()
    designs = []

    for i in range(len(lines)):
        if i == 0:
            patterns = set(lines[i].strip('\n').split(", "))
        elif i == 1:
            continue
        else:
            designs.append(lines[i].strip('\n'))

    file.close()

    return patterns, designs

patterns, designs = parse_input("input.txt")

count = 0
cache = {}

def find_pattern(design, patterns):
    if design in cache:
        return cache[design]

    if not design:
        return 1

    solutions = 0
    for i in range(1, len(design) + 1):
        t = design[:i]
        if t in patterns:
            solutions += find_pattern(design[i:], patterns)

    cache[design] = solutions
    return solutions

# Part 1:
count = 0
for design in designs:
    if find_pattern(design, patterns) > 0:
        count += 1

print(count)

# Part 2:
count = 0
for design in designs:
    count += find_pattern(design, patterns)

print(count)
