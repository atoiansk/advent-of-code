list_1 = []
list_2 = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list_1.append(int(line.split()[0]))
        list_2.append(int(line.split()[1]))

list_1.sort()
list_2.sort()

difference_sum = 0

for i in range(0, len(list_1)):
   difference_sum += abs(list_1[i] - list_2[i])

print(difference_sum)



