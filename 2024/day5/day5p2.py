instructions = {}


with open("input.txt") as file:
    for line in file:
        if "|" in line: 
            key, value = line.strip().split("|")
            if key in instructions:
                instructions[key].append(value)
            else:
                instructions[key] = [value]

def is_valid_update(update, rules):
    was_modified = False 
    while True:
        changed = False
        for key, values in rules.items():
            for value in values:
                if key in update and value in update:
                    key_index = update.index(key)
                    value_index = update.index(value)

                    if key_index > value_index:
                        update[key_index], update[value_index] = update[value_index], update[key_index]
                        changed = True
                        was_modified = True  
        if not changed:
            break
    return update, was_modified

total_middle_pages = 0
with open("input.txt") as file:
    for line in file:
        if "|" not in line and len(line.strip()) > 0: 
            update = line.strip().split(",")
            reordered, was_modified = is_valid_update(update, instructions)
            
            if was_modified:  
                middle_index = len(reordered) // 2
                total_middle_pages += int(reordered[middle_index])  

print(total_middle_pages)
