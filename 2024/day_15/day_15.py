from robot import Robot

def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()

    walls = set()
    boxes = set()
    robot_position = None
    moves = []

    for i in range(len(lines)):
        if lines[i][0] == "#":
            for j in range(len(lines[i])):
                if lines[i][j] == "#":
                    walls.add((j, i))
                elif lines[i][j] == "O":
                    boxes.add((j, i))
                elif lines[i][j] == "@":
                    robot_position = (j, i)
        elif not lines[i].isspace():
            moves += list(lines[i].strip('\n'))

    return moves, Robot(robot_position, walls, boxes)

moves, robot = parse_input("input.txt")

for move in moves:
    robot.move(move)

robot.print_map()
gps = 0

for box in robot.boxes:
    gps += box[0] + 100 * box[1]

print(gps)
