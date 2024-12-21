from utils import get_complexity
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
sum = 0

# Part 1
with timer():
    for line in lines:
        sum += get_complexity(line.strip('\n'))

    print(sum)
