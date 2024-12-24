from utils import parse_input

x_values, y_values, operations = parse_input("input.txt")

highest_z = 'z45'

wrong = set()

for operation in operations:
    input1, input2, op, output = operation

    if output[0] == 'z' and op != 'XOR' and output != highest_z:
        wrong.add(output)

    if op == 'XOR' and output[0] not in ['x', 'y', 'z'] and input1[0] not in ['x', 'y'] and input2[0] not in ['x', 'y']:
        wrong.add(output)

    if op == "AND" and "x00" not in [input1, input2]:
        for subop1, subop2, subop, subres in operations:
            if (output == subop1 or output == subop2) and subop != "OR":
                wrong.add(output)
    if op == "XOR":
        for subop1, subop2, subop, subres in operations:
            if (output == subop1 or output == subop2) and subop == "OR":
                wrong.add(output)

print(','.join(wrong))
