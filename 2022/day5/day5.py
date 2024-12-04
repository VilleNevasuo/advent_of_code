
def arrange(biglist, raw_data, reverse=0):

    copy_list = biglist[:]
    for el in raw_data[10:]:
        el = el.split(" ")
        amount, beg, fin = int(el[1]), int(el[3]), int(el[5])

        to_move = copy_list[beg-1][0:amount]
        if reverse:
            to_move.reverse()

        del copy_list[beg-1][0:amount]

        copy_list[fin-1][:0] = to_move

    s = ""
    for el in copy_list:
        s += el[0]

    return s


raw_data = []
biglist = []

with open("data.txt", "r") as file:
    for line in file:
        raw_data.append(line.strip())

    for i in range(1, 36, 4):
        l = []
        for el in raw_data[:8]:
            if el[i] != " ":
                l.append(el[i])
        biglist.append(l)

    print("part 1:", arrange(biglist, raw_data, reverse=1))
    print("part 2:", arrange(biglist, raw_data))
