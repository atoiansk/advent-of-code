from monkey_market import MonkeyMarket
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {end - start} seconds")

file = open("input.txt", "r")
lines = file.readlines()

# Part 1
with timer():
    sum = 0

    for line in lines:
        initial_number = int(line.strip('\n'))
        sum += MonkeyMarket(initial_number, 2000).get_last_secret_number()

    print(sum)

# Part 2
with timer():
    price_changes_sequences = []
    unique_sequences = set()

    for line in lines:
        initial_number = int(line.strip('\n'))
        price_changes_sequence = MonkeyMarket(initial_number, 2000).get_change_sequences()
        unique_sequences = unique_sequences | set(price_changes_sequence.keys())

        price_changes_sequences.append(price_changes_sequence)

    max_price = -1
    max_price_sequence = []

    for unique_sequence in unique_sequences:
        sum = 0
        for price_changes_sequence in price_changes_sequences:
            if unique_sequence in price_changes_sequence:
                sum += price_changes_sequence[unique_sequence]
        if sum > max_price:
            max_price = sum
            max_price_sequence = unique_sequence

    print(max_price, max_price_sequence)
