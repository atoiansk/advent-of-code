count = 0

def check_rules(item, previous_item, increase, decrease):
    if previous_item == item:
        return False

    if abs(previous_item - item) > 3:
        return False

    if previous_item > item:
        if increase:
            return False
        decrease = True

    if previous_item < item:
        if decrease:
            return False
        increase = True

    return True

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        items = line.split()
        previous_item = int(-1)
        decrease = False
        increase = False
        safe = True

        for item in items:
            item = int(item)

            if previous_item == -1:
                previous_item = item
                continue;

            result = check_rules(item, previous_item, increase, decrease)

            if result and previous_item > item:
                decrease = True
            elif result and previous_item < item:
                increase = True
            else:
                safe = False
                break;

            previous_item = item

        if safe:
            print(items)
            count += 1

print(count)




