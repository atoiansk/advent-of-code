from utils import parse_input, calculate_check_sum

def compact_data(memory):
    move_index = 0

    for i in reversed(range(len(memory))):
        if memory[i] == '.':
            continue;

        while memory[move_index] != '.':
            move_index += 1

        if move_index >= i:
            break;

        memory[move_index] = memory[i]
        memory[i] = '.'
    return memory


memory = parse_input('input.txt')

print(calculate_check_sum(compact_data(memory)))







