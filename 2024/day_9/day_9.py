def parse_input(file_name):
    file = open(file_name, 'r')
    line = file.readline().strip('\n')

    result = []
    block_id = 0

    for i in range(len(line)):
        char = line[i]

        if i % 2 == 0:
            for j in range(int(char)):
                result.append(block_id)
            block_id += 1
        else:
            for j in range(int(char)):
                result.append('.')
    return result

def calculate_check_sum(compacted_memory):
    check_sum = 0

    for i in range(len(compacted_memory)):
        char = compacted_memory[i]

        if char == '.':
            continue

        check_sum += int(char) * i
    return check_sum

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







