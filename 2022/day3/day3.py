
total1 = 0
total2 = 0
group_string = ""
groups = []


def increment_total(intersect, total):
    for el in intersect:
        if el.islower():
            total += ord(el) - 96
        else:
            total += ord(el.lower()) - 70

    return total


with open("data.txt", "r") as file:
    for count, line in enumerate(file):

        firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]

        groups.append(line.strip())

        intersect = set(firsthalf).intersection(secondhalf)

        if len(groups) % 3 == 0:
            intersect2 = set(groups[0]) & set(groups[1]) & set(groups[2])
            total2 = increment_total(intersect2, total2)
            groups.clear()

        total1 = increment_total(intersect, total1)

    print(total1)
    print(total2)

    # attempt to refactor with list comp
    # total = sum([ord(el)-96 if el.islower() else ord(el.lower())-70
    #              for el in intersect])
