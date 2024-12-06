import guard
import parse_grid

grid, start_position, start_direction = parse_grid.parse_grid('input.txt')

guard = guard.Guard(start_position, start_direction, grid)

grid_x, grid_y = len(grid), len(grid[0])

position_history = set()

while True:
    try:
        guard.move()
        position_history.add(guard.position)
    except Exception as e:
        break

print(len(position_history))

