

def move_vertically(matrix, line, head_pos, tail_pos):

    to_move = int(line[1])
    for i in range(to_move):
        if line[0] == "U":
            head_pos[0] -= 1
            if tail_pos[0] - head_pos[0] > 1:
                if head_pos[1] != tail_pos[1]:
                    tail_pos[1] = head_pos[1]
                tail_pos[0] -= 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"
        else:
            head_pos[0] += 1
            if head_pos[0] - tail_pos[0] > 1:
                if head_pos[1] != tail_pos[1]:
                    tail_pos[1] = head_pos[1]
                tail_pos[0] += 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"

    return head_pos, tail_pos, matrix


def move_horizontally(matrix, line, head_pos, tail_pos):

    to_move = int(line[1])
    for i in range(to_move):
        if line[0] == "R":
            head_pos[1] += 1
            if head_pos[1] - tail_pos[1] > 1:
                if head_pos[0] != tail_pos[0]:
                    tail_pos[0] = head_pos[0]
                tail_pos[1] += 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"
        else:
            head_pos[1] -= 1
            if tail_pos[1] - head_pos[1] > 1:
                if head_pos[0] != tail_pos[0]:
                    tail_pos[0] = head_pos[0]
                tail_pos[1] -= 1
                matrix[tail_pos[0]][tail_pos[1]] = "#"

    return head_pos, tail_pos, matrix


matrix = [["." for i in range(800)] for j in range(800)]
count = 0

head_pos = [400, 400]
tail_pos = [400, 400]


matrix[tail_pos[0]][tail_pos[1]] = "#"

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "U" or line[0] == "D":
            head_pos, tail_pos, matrix = move_vertically(
                matrix, line, head_pos, tail_pos)
        else:
            head_pos, tail_pos, matrix = move_horizontally(
                matrix, line, head_pos, tail_pos)


for line in matrix:
    for el in line:
        if el == "#":
            count += 1
print("tiles visited", count)
