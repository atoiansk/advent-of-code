class Map:
    def __init__(self, m, n, antenas):
        self.m = m
        self.n = n
        self.antenas = antenas

    def get_antinodes(self, all=False):
        antinodes = set()

        for antena in self.antenas.values():
            for i in range(len(antena)):
                for j in range(i + 1, len(antena)):
                    antinodes = antinodes | self.get_antinodes_for_antena_pair(antena[i],antena[j],all)
        return antinodes

    def get_antinodes_for_antena_pair(self, antena_1, antena_2, all):
        distance_x = antena_1[0] - antena_2[0]
        distance_y = antena_1[1] - antena_2[1]

        antinodes = set()

        antinodes_1 = self.get_antinode_for_antena(antena_1, distance_x, distance_y, all)
        antinodes_2 = self.get_antinode_for_antena(antena_2, -distance_x, -distance_y, all)

        antinodes = antinodes | antinodes_1 | antinodes_2

        return antinodes

    def get_antinode_for_antena(self, antena, distance_x, distance_y, all):
        antinodes = set()
        i = 0
        node = antena

        while not self.out_of_bounds(node):
            if i > 0 or all:
                antinodes.add(node)

            if not all and i == 1:
                break

            i += 1
            node = (antena[0] + distance_x * i, antena[1] + distance_y * i)
        return antinodes

    def out_of_bounds(self, node):
        if node[0] < 0 or node[1] < 0:
            return True

        if node[0] >= self.m or node[1] >= self.n:
            return True

        return False

    def print_grid(self, all=False):
        antinodes = self.get_antinodes(all)

        for i in range(self.m):
            for j in range(self.n):
                if any((i,j) in arr for arr in self.antenas.values()):
                    matching_keys = [key for key, array in self.antenas.items() if (i,j) in array]
                    print(matching_keys[0], end='')
                elif (i,j) in antinodes:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
