from utils import parse_input

moves, robot = parse_input("input.txt")

for move in moves:
    robot.move(move)

robot.print_map()
gps = 0

for box in robot.boxes:
    gps += box[0] + 100 * box[1]

print(gps)
