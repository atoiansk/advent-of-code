from utils import parse_input
from program import Program
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {end - start} seconds")

program = parse_input('input.txt')

target_output = program.code

with timer():
    valid_values_for_a = set()
    valid_values_for_a.add(None)
    for i in range(len(target_output)):
        target_value = target_output[-(i+1)]
        valid_values_for_a_copy = valid_values_for_a.copy()
        valid_values_for_a = set()

        for last_digit in valid_values_for_a_copy:
            for j in range(8):
                if last_digit is None:
                    input = j
                else:
                    input = last_digit * 8 + j

                # Only one loop
                new_program = Program(input, 0, 0, program.code[:len(program.code)-2])
                output = new_program.run()

                if output[0] == target_value:
                    valid_values_for_a.add(input)

    print(min(valid_values_for_a))


