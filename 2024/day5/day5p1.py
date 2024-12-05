
instructions = {}

with open("input.txt") as file:
    for line in file:
        if "|" in line:  
            key, value = line.strip().split("|")
            if key in instructions:
                instructions[key].append(value)
            else:
                instructions[key] = [value]
        else:  
            updates = line.strip().split(",")

def is_valid_update(update, rules):
   
   while True:
        for key, values in rules.items():
            for value in values:
                if key in update and value in update:
                    if update.index(key) > update.index(value):
                        return False
        return True

total_middle_pages = 0
with open("input.txt") as file:
    for line in file:
        if "|" not in line and len(line) > 1: 
            update = line.strip().split(",")
            
            if is_valid_update(update, instructions):
                middle_index = len(update) // 2
                total_middle_pages += int(update[middle_index])

print(total_middle_pages)
