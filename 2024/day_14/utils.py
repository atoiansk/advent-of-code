from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {end - start} seconds")

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

    def move(self, times):
        x, y = self.position
        vx, vy = self.velocity

        new_x = (x + vx * times) % self.grid_size[0]
        new_y = (y + vy * times) % self.grid_size[1]

        self.position = (new_x, new_y)

class Grid:
    def __init__(self, grid_size, robots):
        self.grid_size = grid_size
        self.robots = robots
        self.quadrant_factors = [0, 0, 0, 0]

    def move_robots(self, seconds):
        for robot in self.robots:
            robot.move(seconds)

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
