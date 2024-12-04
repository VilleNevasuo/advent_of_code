

def calculate_vertices(instructions):
    total = 0
    x, y = 0, 0
    vertices = [(x, y)]
    for distance, direction in instructions:
        total += distance
        if direction == "R":
            x += distance
        elif direction == "D":
            y -= distance
        elif direction == "L":
            x -= distance
        elif direction == "U":
            y += distance
        vertices.append((x, y))

    return vertices, total


def shoelace_formula(vertices):

    
    x_sum = 0
    y_sum = 0
    for i in range(len(vertices)):
        if i+1 < len(vertices):
            x_sum += vertices[i][0] * vertices[i+1][1]
            y_sum += vertices[i][1] * vertices[i+1][0]
    return abs(x_sum-y_sum)/2


def picks_theorem(area,perimeter):

    return area-(1/2)*perimeter+1




instructions = []

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        line = line[2]
        line = line.strip("()#")
        distance = int(line[:5],16)
        dir = int(line[-1])
        directions = ["R", "D", "L", "U"]
        dir = directions[dir]
        instructions.append((distance,dir))


vertices, total_perimeter = calculate_vertices(instructions)

area = shoelace_formula(vertices)

finito = picks_theorem(area,total_perimeter)
print("picks",finito+total_perimeter)
