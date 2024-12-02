list_1 = []
list_2 = {}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        list_1.append(int(line.split()[0]))

        list_2_key = int(line.split()[1])

        if list_2_key in list_2:
            list_2[list_2_key] += 1
        else:
            list_2[list_2_key] = 1

similarity_sum = 0

for item in list_1:
    if item in list_2:
        print(item, list_2[item])
        similarity_sum += item * list_2[item]

print(similarity_sum)


