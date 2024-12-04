<<<<<<< HEAD

total = 0
scoring_a = {"AY": 8, "AX": 4, "AZ": 3, "BY": 5,
             "BX": 1, "BZ": 9, "CY": 2, "CX": 7, "CZ": 6}
scoring_b = {"AY": 4, "AX": 3, "AZ": 8, "BY": 5,
             "BX": 1, "BZ": 9, "CY": 6, "CX": 2, "CZ": 7}

with open("data.txt", "r") as file:
    for line in file:
        s = "".join(line.split())
        total += scoring_b[s]

print(total)
=======

total = 0
scoring_a = {"AY": 8, "AX": 4, "AZ": 3, "BY": 5,
             "BX": 1, "BZ": 9, "CY": 2, "CX": 7, "CZ": 6}
scoring_b = {"AY": 4, "AX": 3, "AZ": 8, "BY": 5,
             "BX": 1, "BZ": 9, "CY": 6, "CX": 2, "CZ": 7}

with open("data.txt", "r") as file:
    for line in file:
        s = "".join(line.split())
        total += scoring_b[s]

print(total)
>>>>>>> e481f32ca53b50252269e71134bdc26e3879ff2a
