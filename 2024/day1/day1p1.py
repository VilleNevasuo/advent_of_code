left = []
right = []
pairs = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))

while len(left) != 0:

    min_left = min(left)
    min_right = min(right)

    pairs.append((min_left, min_right))

    right.remove(min_right)
    left.remove(min_left)

print(pairs)

total = 0

for pair in pairs:
    distance = abs(pair[1] - pair[0])  # Calculate absolute distance
    total += distance

print(total)
