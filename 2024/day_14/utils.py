def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()

    positions = []
    velocities = []

    for line in lines:
        aux = line.strip('\n').split(' ')
        position = aux[0].split('p=')[1].split(',')
        velocity = aux[1].split('v=')[1].split(',')

        positions.append((int(position[0]), int(position[1])))
        velocities.append((int(velocity[0]), int(velocity[1])))

    return positions, velocities

class Robot:
    def __init__(self, grid_size, position, velocity):
        self.grid_size = grid_size
        self.position = position
        self.velocity = velocity

    def move(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

        x, y = self.position
        grid_x, grid_y = self.grid_size

        wrapped_x = x % grid_x
        wrapped_y = y % grid_y

        self.position = (wrapped_x, wrapped_y)

class Grid:
    quadrant_factors = [0, 0, 0, 0]

    def __init__(self, grid_size, robots):
        self.grid_size = grid_size
        self.robots = robots

    def move_robots(self, seconds):
        for robot in self.robots:
            for _ in range(seconds):
                robot.move()

            quadrant = self.find_quadrant(robot.position[0], robot.position[1])

            if quadrant is not None:
                self.quadrant_factors[quadrant] += 1

    def safety_factor(self):
        safety_factor = 1

        for factor in self.quadrant_factors:
            safety_factor *= factor

        return safety_factor

    def find_quadrant(self, x, y):
        half_x = self.grid_size[0] // 2
        half_y = self.grid_size[1] // 2

        if x < half_x and y < half_y:
            return 0
        elif x < half_x and y > half_y:
            return 2
        elif x > half_x and y < half_y:
            return 1
        elif x > half_x and y > half_y:
            return 3

    def print_grid(self):
        robots_positions = [robot.position for robot in self.robots]

        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                if (j, i) in robots_positions:
                    print(robots_positions.count((j, i)), end='')
                else:
                    print('.', end='')
            print()
        return
