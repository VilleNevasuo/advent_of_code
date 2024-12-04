

def move_head(head, direction):

    if direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1
    elif direction == "L":
        head[0] -= 1
    else:
        head[0] += 1


def is_touching(head, tail):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2


def move_tail(tail, head):
    if head[0] > tail[0]:
        tail[0] += 1
    if head[0] < tail[0]:
        tail[0] -= 1
    if head[1] > tail[1]:
        tail[1] += 1
    if head[1] < tail[1]:
        tail[1] -= 1


knots = [[0, 0] for i in range(10)]

visited = set()


with open("data.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        for i in range(int(line[1])):

            move_head(knots[0], line[0])
            for i in range(1, len(knots)):
                if not is_touching(knots[i], knots[i-1]):
                    move_tail(knots[i], knots[i-1])

            visited.add(tuple(knots[9]))

print(len(visited))
