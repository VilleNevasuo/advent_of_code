
floor = 0


with open("input.txt") as file:
    for line in file:
        for i,char in enumerate(line):
            if char == "(":
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                print(i)
print(floor)