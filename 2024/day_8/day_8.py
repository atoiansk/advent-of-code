from utils import parse_input, print_grid, out_of_bounds

def get_antinodes(antena_1, antena_2, m, n):
    distance_x = antena_1[0] - antena_2[0]
    distance_y = antena_1[1] - antena_2[1]

    antinodes = set()

    antinode_1 = (antena_1[0] + distance_x, antena_1[1] + distance_y)

    if not out_of_bounds(antinode_1, m, n):
        antinodes.add(antinode_1)

    antinode_2 = (antena_2[0] - distance_x, antena_2[1] - distance_y)

    if not out_of_bounds(antinode_2, m, n):
        antinodes.add(antinode_2)

    return antinodes

antenas, m, n = parse_input('input.txt')

antinodes = set()

for antena in antenas.values():
    for i in range(len(antena)):
        for j in range(i + 1, len(antena)):
            antinodes = antinodes | get_antinodes(antena[i],antena[j],m,n)

print(len(antinodes))

# print_grid(m,n,antenas,antinodes)


