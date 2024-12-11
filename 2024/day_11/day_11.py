from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {end - start} seconds")

def parse_input(filename):
    file = open(filename, 'r')
    line = file.readline().split()
    list = []

    for char in line:
        list.append(int(char))

    return list

map = {}

def blink(element, times):
    if (element, times) in map:
        return map[(element, times)]

    if times == 0:
        return 1

    if element == 0:
        map[(element, times)] = blink(1, times - 1)
        return blink(1, times - 1)
    elif len(str(element)) % 2 == 0:
        string = str(element)
        middle = len(string) // 2
        map[(element, times)] = blink(int(string[:middle]), times - 1) + blink(int(string[middle:]), times - 1)
        return blink(int(string[:middle]), times - 1) + blink(int(string[middle:]), times - 1)
    else:
        map[(element, times)] = blink(element * 2024, times - 1)
        return blink(element * 2024, times - 1)

def blink_all(list, n_blinks):
    result = 0

    for element in list:
        result += blink(element, n_blinks)

    return result

list = parse_input('input.txt')

with timer():
    # Part 1
    print(blink_all(list, 25))

with timer():
    # Part 2
    print(blink_all(list, 75))


