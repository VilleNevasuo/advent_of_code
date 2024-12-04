

def hashing(element):

    current_value = 0
    for char in element:
        current_value += ord(char)
        current_value = current_value*17
        current_value = current_value%256

    return current_value


def p1():
    total = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split(",")
            for el in line:
                current_value = 0
                current_value = hashing(el)
                total += current_value
    return total

def p2():

    boxes = {box_number: [] for box_number in range(256)}
    total = 0
    with open("input.txt") as file:
        for line in file:
            sequences = line.strip().split(",")
            for el in sequences:
                operation = "-" if "-" in el else "="
                if "=" in el:
                    box = hashing(el[:-2])
                    label = el[:-2] + " " + el[-1]
                    focal_length = el[-1]
                else:
                    box = hashing(el[:-1])
                    label = el[:-1] 

                prefix = label.split()[0]
                if operation == "-":
                    boxes[box] = [item for item in boxes[box] if not item.startswith(label + " ")]
                else:
                    if any(item.startswith(prefix + " ") for item in boxes[box]):
                        boxes[box] = [label if item.startswith(prefix + " ") else item for item in boxes[box]]
                    else:
                        boxes[box].append(label)


            for box_number, items in boxes.items():
                for index, item in enumerate(items):
                    boxadd = box_number+1
                    indexadd = int(index)+1
                    focaladd = int(item[-1])
                    subtotal = boxadd*indexadd*focaladd
                    total += subtotal
                
    return total
        

print(p1())
print(p2())

