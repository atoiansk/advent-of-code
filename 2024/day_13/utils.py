def parse_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()

    a_move = []
    b_move = []
    prizes = []

    for line in lines:
        line = line.strip('\n')

        if line.startswith('Button A'):
            x, y = line.split('X+')[1].split(',')[0], line.split('Y+')[1].split(' ')[0]
            a_move.append((int(x), int(y)))
        elif line.startswith('Button B'):
            x, y = line.split('X+')[1].split(',')[0], line.split('Y+')[1].split(' ')[0]
            b_move.append((int(x), int(y)))
        elif line.startswith('Prize'):
            x, y = line.split('X=')[1].split(',')[0], line.split('Y=')[1].split(' ')[0]
            prizes.append((int(x), int(y)))

    return a_move, b_move, prizes

def solve_system(a_move, b_move, prize):
    times_b = (prize[1]*a_move[0] - a_move[1]*prize[0]) / (b_move[1]*a_move[0] - a_move[1]*b_move[0])
    times_a = (prize[0] - b_move[0]*times_b) / a_move[0]
    return times_a, times_b
