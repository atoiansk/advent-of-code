def get_input():
    file = open('input.txt', 'r')
    return file.readlines()

def check_safe(array):
    max_distance = max(abs(a-b) for a, b in zip(array, array[1:]))
    all_desc = all(a > b for a,b in zip(array, array[1:]))
    all_inc = all(a < b for a,b in zip(array, array[1:]))

    return max_distance <= 3 and (all_desc or all_inc)


lines = get_input()
count = 0

for line in lines:
    items = []
    items.append([int(s) for s in line.split()])
    items = items[0]

    safe = check_safe(items)

    if not safe:
        for index in range(len(items)):
            items_copy = items.copy()
            items_copy.pop(index)
            safe = check_safe(items_copy)

            if safe:
                break;

    if safe:
        count += 1

print(count)




