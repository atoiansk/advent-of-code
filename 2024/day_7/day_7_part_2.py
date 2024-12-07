from parse_input import parse_input

def validate_equation(test_value, numbers):
    results = set()
    results.add(numbers[0])

    for i in range(1, len(numbers)):
        results_copy = results.copy()
        results.clear()

        for result in results_copy:
            mult = result * numbers[i]
            sum = result + numbers[i]
            concat = int(str(result) + str(numbers[i]))

            if i == len(numbers) - 1 and (test_value == mult or test_value == sum or test_value == concat):
                return True
            else:
                results.add(mult)
                results.add(sum)
                results.add(concat)

    return False

test_values, numbers_array = parse_input('input.txt')

sum = 0

for i in range(len(numbers_array)):
    valid = validate_equation(test_values[i], numbers_array[i])

    if valid:
        sum += test_values[i]

print(sum)
