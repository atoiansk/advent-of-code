import re

def get_input():
    file = open('input.txt', 'r')
    return file.read()

def with_regex(text):
    matches = re.findall(r'mul\((\d+),(\d+)\)', text)

    sum = 0

    for num1, num2 in matches:
        sum += int(num1) * int(num2)

    return sum

text = get_input().split("don't")

enabled = True

sum = 0

for block in text:
    do_blocks = block.split("do")
    for do_block in do_blocks:
        if enabled:
            sum += with_regex(do_block)
        enabled = True
    enabled = False


print(sum)
