def get_input():
    file = open('input.txt', 'r')
    lines = file.readlines()

    rules, updates = [], []

    array = rules

    for line in lines:
        if line.strip('\n') == "":
            array = updates
            continue

        array.append(line.strip('\n'))

    rules = [rule.split('|') for rule in rules]
    updates = [update.split(',') for update in updates]

    return rules, updates

def get_corrected_invalid_updates():
    rules, updates = get_input()
    invalid_update_indexes = []

    i = 0

    while i < len(updates):
        valid = True
        update = updates[i]

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = False
                    index_0 = update.index(rule[0])
                    index_1 = update.index(rule[1])
                    aux = update[index_0]
                    update[index_0] = update[index_1]
                    update[index_1] = aux
                    break;

        if not valid:
            if i not in invalid_update_indexes:
                invalid_update_indexes.append(i)
        else:
            i += 1

    corrected_updates = [updates[i] for i in invalid_update_indexes]

    return corrected_updates

def get_middle_page(update):
    length = len(update)
    return update[length // 2]

sum = 0

for update in get_corrected_invalid_updates():
    sum += int(get_middle_page(update))

print(sum)

# print(get_corrected_invalid_updates())


