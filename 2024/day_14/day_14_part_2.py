from utils import parse_input, Robot, Grid, timer
import sys

positions, velocities = parse_input('input.txt')
grid_size = (101, 103)

minimum_score = sys.maxsize
i_at_minimum_score = 0

with timer():
    for i in range(101*103):
        robots = [Robot(grid_size, positions[i], velocities[i]) for i in range(len(positions))]
        grid = Grid(grid_size, robots)
        grid.move_robots(i)

        score = grid.safety_factor()
        if score < minimum_score:
            minimum_score = score
            i_at_minimum_score = i

    robots = [Robot(grid_size, positions[i], velocities[i]) for i in range(len(positions))]
    grid = Grid(grid_size, robots)
    grid.move_robots(i_at_minimum_score)
    grid.print_grid()

    print(i_at_minimum_score)
