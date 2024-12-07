def parse_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    test_value = []
    numbers = []

    for line in lines:
        test_value.append(int(line.split(':')[0]))
        numbers.append(list(map(int, line.split(':')[1].split())))

    return test_value, numbers
