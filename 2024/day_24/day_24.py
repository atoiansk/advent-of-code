from utils import parse_input

def run_operations(values, operations):
    z_values = {}
    local_values = values

    while operations:
        input1, input2, op, output = operations.pop()

        if input1 in local_values and input2 in local_values:
            match op:
                case "OR":
                    local_values[output] = local_values[input1] | local_values[input2]
                case "AND":
                    local_values[output] = local_values[input1] & local_values[input2]
                case "XOR":
                    local_values[output] = local_values[input1] ^ local_values[input2]

            if output[0] == "z":
                z_values[output] = local_values[output]
        else:
            operations.appendleft([input1, input2, op, output])

    return z_values

def binary_to_decimal(binary, char):
    sum = 0

    for key, value in binary.items():
        index = int(key.split(char)[1])
        sum += value * (2 ** index)

    return sum

x_values, y_values, operations = parse_input("input.txt")

values = {**x_values, **y_values}

z_values = run_operations(values, operations)

result = binary_to_decimal(z_values, "z")

print(result)
