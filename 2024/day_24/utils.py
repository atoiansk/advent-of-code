from collections import deque

def parse_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    x_values = {}
    y_values = {}
    operations = deque()
    flag_operations = False

    for line in lines:
        if line == "\n":
            flag_operations = True
            continue

        if not flag_operations:
            value = line.split(":")[0]

            if value[0] == "x":
                x_values[value] = int(line.split(":")[1].strip())
            else:
                y_values[value] = int(line.split(":")[1].strip())
        else:
            input1 = line.split(' ')[0].strip()
            op = line.split(' ')[1].strip()
            input2 = line.split(' ')[2].strip()
            output = line.split('-> ')[1].strip()
            operations.appendleft([input1, input2, op, output])

    return x_values, y_values, operations
