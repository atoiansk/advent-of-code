from utils import get_code_cost
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {end - start} seconds")

file = open("input.txt", 'r')
lines = file.readlines()

# Part 1
with timer():
    sum = 0
    for line in lines:
        complexity = get_code_cost(line.strip('\n')) * int(line.strip('A\n'))
        sum += complexity

    print(sum)

# Part 2
with timer():
    sum = 0
    for line in lines:
        complexity = get_code_cost(line.strip('\n'),25) * int(line.strip('A\n'))
        sum += complexity

    print(sum)




