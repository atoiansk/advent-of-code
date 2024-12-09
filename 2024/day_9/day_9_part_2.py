def parse_input(file_name):
    file = open(file_name, 'r')
    line = file.readline().strip('\n')

    files = {}
    empty_spaces = []
    block_id = 0
    cumulative_index = 0

    for i in range(len(line)):
        char = line[i]

        if i % 2 == 0:
            files.setdefault(block_id, [cumulative_index, int(char)])
            block_id += 1
        else:
            if int(char) == 0:
                continue
            empty_spaces.append([cumulative_index, int(char)])

        cumulative_index += int(char)
    return files, empty_spaces

def compact_data(files, empty_spaces):
    for key, value in reversed(files.items()):
        file_start_index, file_length = value

        for i in range(len(empty_spaces)):
            empty_start_index, empty_length = empty_spaces[i]

            if empty_start_index >= file_start_index:
                continue

            if empty_length < file_length:
                continue

            new_start_index = empty_start_index + file_length
            new_length = empty_length - file_length
            empty_spaces[i] = [new_start_index, new_length]
            files[key] = [empty_start_index, file_length]

            break;
    return files

def calculate_check_sum(compacted_files):
    check_sum = 0

    for key, value in files.items():
        start_index, length = value

        for i in range(length):
            check_sum += int(key) * (start_index + i)

    return check_sum

files, empty_spaces = parse_input('input.txt')
compacted_files = compact_data(files, empty_spaces)

# print(compacted_files)
print(calculate_check_sum(compacted_files))
