from utils import parse_input, Robot, Grid

positions, velocities = parse_input('test_input.txt')
grid_size = (11, 7)

robots = [Robot(grid_size, positions[i], velocities[i]) for i in range(len(positions))]
grid = Grid(grid_size, robots)
grid.move_robots(100)
grid.print_grid()

