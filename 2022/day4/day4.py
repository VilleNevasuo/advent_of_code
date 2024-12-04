
full_overlap = 0
partial_overlap = 0

with open("data.txt", "r") as file:
    for line in file:

        values = line.strip().split(",")
        s = "-".join(values)
        values = s.split("-")
        values = [int(i) for i in values]

        if values[0] < values[2] and values[1] < values[3]:
            pass
        elif values[0] > values[2] and values[1] > values[3]:
            pass
        else:
            full_overlap += 1

        if values[1] < values[2] or values[0] > values[3]:
            pass
        else:
            partial_overlap += 1
        values.clear()

    print(full_overlap)
    print(partial_overlap)
