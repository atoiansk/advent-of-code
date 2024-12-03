import re

def get_input():
    file = open('input.txt', 'r')
    return file.read()

def with_regex():
    matches = re.findall(r'mul\((\d+),(\d+)\)', get_input())

    sum = 0

    for num1, num2 in matches:
        sum += int(num1) * int(num2)

    return sum

def without_regex():
    text = get_input()
    match = ['m','u','l','(']

    index = 0;

    isNumber1 = False
    isNumber2 = False

    number1String = ''
    number2String = ''

    sum = 0

    for char in text:
        if isNumber1:
            if char.isdigit():
                number1String += char
            elif char == ',' and number1String != '':
                isNumber1 = False
                isNumber2 = True
            else:
                isNumber1 = False
                index = 0
                number1String = ''
                number2String = ''
        elif isNumber2:
            if char.isdigit():
                number2String += char
            elif char == ')' and number2String != '':
                isNumber2 = False
                index = 0
                sum += int(number1String) * int(number2String)
                number1String = ''
                number2String = ''
            else:
                isNumber2 = False
                index = 0
                number1String = ''
                number2String = ''
        else:
            if char == match[index]:
                if char == '(':
                    isNumber1 = True
                index += 1
            else:
                index = 0
                isNumber1 = False
                isNumber2 = False

    return sum



print(with_regex())

print(without_regex())
