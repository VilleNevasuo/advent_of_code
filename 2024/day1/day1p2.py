
from collections import Counter

left = []
right = []
pairs = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))

similarity_score = 0

for l in left:
    count_in_right = right.count(l)
    similarity_score += l * count_in_right

print(similarity_score)