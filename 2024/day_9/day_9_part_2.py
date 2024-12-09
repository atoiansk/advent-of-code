from utils import parse_input, calculate_check_sum

def compact_data(memory):
    i = len(memory) - 1

    while i > 0:
        print(i)
        if memory[i] == '.':
            i -= 1
            continue;

        current_id = memory[i]
        i_start = i

        while memory[i_start] == current_id:
            i_start -= 1
        length = i - i_start

        empty_space = find_empty_space(memory, i_start + 1, length)

        i = i_start

        if len(empty_space) > 0:
            memory = move_file(memory, i_start + 1, empty_space[0], length)

    return memory

def find_empty_space(memory, file_start_index, file_len):
    i = 0
    while i < file_start_index:
        if memory[i] != '.':
            i += 1
            continue

        end_i = i
        while memory[end_i] == '.':
           end_i += 1

        len = end_i - i

        if len >= file_len:
            return [i, end_i - 1]
        else:
            i = end_i
    return []

def move_file(memory, file_start_index, empty_start_index, file_length):
    for i in range (file_length):
        memory[empty_start_index + i] = memory[file_start_index + i]
        memory[file_start_index + i] = '.'
    return memory

memory = parse_input('input.txt')

print(calculate_check_sum(compact_data(memory)))
