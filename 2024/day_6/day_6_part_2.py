from guard import Guard
import parse_grid

def detect_loop(guard):
    position_history = set()

    while True:
        try:
            guard.move()

            if (guard.position, guard.direction) in position_history:
                return True
            else:
                position_history.add((guard.position, guard.direction))
        except Exception as e:
            return False

grid, start_position, start_direction = parse_grid.parse_grid('input.txt')

guard = Guard(start_position, start_direction, grid)

new_obstacles = set()
i = 0

while True:
    obstacle_x = guard.position[0] + Guard.direction_movements[guard.direction][0]
    obstacle_y = guard.position[1] + Guard.direction_movements[guard.direction][1]

    grid_copy = [row[:] for row in grid]

    try:
        grid_copy[obstacle_x][obstacle_y] = '#'
    except Exception as e:
        break

    new_guard = Guard(start_position, start_direction, grid_copy)

    if detect_loop(new_guard):
        new_obstacles.add((obstacle_x, obstacle_y))

    try:
        guard.move()
    except Exception as e:
        break


print(len(new_obstacles))
