class Guard:
    directions = ['^', '>', 'v', '<']
    direction_movements = [[-1, 0],[0, 1],[1, 0],[0, -1]]
    position_history = []

    def __init__(self, start_position, start_direction, grid):
        self.position = start_position
        self.direction = self.directions.index(start_direction)
        self.grid = grid
        self.position_history = set()
        self.position_history.add(start_position)

    def move(self):
        x_movement = self.direction_movements[self.direction][0]
        y_movement = self.direction_movements[self.direction][1]

        new_position = (self.position[0] + x_movement, self.position[1] + y_movement)

        if self.should_turn(new_position):
            self.turn()
        elif self.out_of_bounds(new_position):
            raise Exception('Out of bounds')
        else:
            self.position = new_position
            self.position_history.add(new_position)

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def should_turn(self, new_position):
        return self.grid[new_position[0]][new_position[1]] == '#'

    def out_of_bounds(self, new_position):
        return new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(self.grid) or new_position[1] >= len(self.grid[0])

    def print_grid(self):
        print(self.position)
        print(self.directions[self.direction])
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.position == (row, col):
                    print(self.directions[self.direction], end='')
                elif (row, col) in self.position_history:
                    print('X', end='')
                elif self.grid[row][col] == '#':
                    print('#', end='')
                else:
                    print('.', end='')
            print()
