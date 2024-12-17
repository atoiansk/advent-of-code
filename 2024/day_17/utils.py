from program import Program

def parse_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()

    reg_a = 0
    reg_b = 0
    reg_c = 0
    code = []

    for line in lines:
        if line.startswith('Register A:'):
            reg_a = int(line.split(':')[1].strip())
        elif line.startswith('Register B:'):
            reg_b = int(line.split(':')[1].strip())
        elif line.startswith('Register C:'):
            reg_c = int(line.split(':')[1].strip())
        elif line.startswith('Program:'):
            code = list(map(int, line.split(':')[1].strip().split(',')))

    return Program(reg_a, reg_b, reg_c, code)
