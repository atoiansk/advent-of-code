from collections import deque

def parse_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    values = {}
    operations = deque()
    flag_operations = False

    for line in lines:
        if line == "\n":
            flag_operations = True
            continue

        if not flag_operations:
            values[line.split(":")[0]] = int(line.split(":")[1].strip())
        else:
            input1 = line.split(' ')[0].strip()
            op = line.split(' ')[1].strip()
            input2 = line.split(' ')[2].strip()
            output = line.split('-> ')[1].strip()
            operations.appendleft([input1, input2, op, output])

    return values, operations

values, operations = parse_input("input.txt")
z_values = {}

while operations:
    input1, input2, op, output = operations.pop()

    if input1 in values and input2 in values:
        match op:
            case "OR":
                values[output] = values[input1] | values[input2]
            case "AND":
                values[output] = values[input1] & values[input2]
            case "XOR":
                values[output] = values[input1] ^ values[input2]

        if output[0] == "z":
            z_values[output] = values[output]
    else:
        operations.appendleft([input1, input2, op, output])

ordered_z_values = {k: z_values[k] for k in sorted(z_values)}

result = 0

for key, value in ordered_z_values.items():
    index = int(key.split('z')[1])
    result += value * (2 ** index)

print(result)
