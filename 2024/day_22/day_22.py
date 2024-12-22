from monkey_market import MonkeyMarket

file = open("input.txt", "r")
lines = file.readlines()

# Part 1
sum = 0

for line in lines:
    initial_number = int(line.strip('\n'))
    sum += MonkeyMarket(initial_number, 2000).get_secret_number()

print(sum)
