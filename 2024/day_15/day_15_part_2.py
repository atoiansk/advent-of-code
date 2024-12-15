from robot_2 import Robot2 as Robot

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
                    walls.add((j*2, i))
                    walls.add((j*2 + 1, i))
                elif lines[i][j] == "O":
                    boxes.add(((j*2, i),(j*2 + 1, i)))
                elif lines[i][j] == "@":
                    robot_position = (j*2, i)
        elif not lines[i].isspace():
            moves += list(lines[i].strip('\n'))

    return moves, Robot(robot_position, walls, boxes)

moves, robot = parse_input("input.txt")

for move in moves:
    robot.move(move)
gps = 0

for box in robot.boxes:
    box_start, box_end = box
    gps += box_start[0] + 100 * box_start[1]

print(gps)
