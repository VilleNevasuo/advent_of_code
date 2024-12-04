

def flood_fill(matrix, start, fill_value):

    rows, cols = len(matrix), len(matrix[0])
    x_start, y_start = start
    original_value = matrix[x_start][y_start]

    if original_value == fill_value:
        return

    stack = [(x_start, y_start)]

    while stack:
        x, y = stack.pop()

        matrix[x][y] = fill_value

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == original_value:
                stack.append((nx, ny))


def p1():

    total = 0
    grid = [["." for _ in range(800)] for _ in range(800)]

    x = 400
    y = 400
    start_x = x + 1
    start_y = y + 1
    grid[x][y] = "#"
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split(" ")
            for i in range(int(line[1])):
                match line[0]:
                        case "R":
                            y += 1
                            grid[x][y] = "#"
                        case "L":
                            y -= 1
                            grid[x][y] = "#"
                        case "U":
                            x -= 1
                            grid[x][y] = "#"
                        case "D":
                            x += 1
                            grid[x][y] = "#"


    flood_fill(grid,(start_x,start_y), "O")

    for line in grid:
        print(line)


    for line in grid:
        for el in line:
            if el == "#" or el == "O":
                total += 1
    return total





print(p1())