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

def get_valid_updates():
    rules, updates = get_input()
    valid_updates = []

    for update in updates:
        valid = True

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = False
                    break;

        if valid:
            valid_updates.append(update)

    return valid_updates

def get_middle_page(update):
    length = len(update)
    return update[length // 2]


sum = 0

for update in get_valid_updates():
    sum += int(get_middle_page(update))

print(sum)

