from collections import Counter



def p1():

    grid = []
    with open("input.txt") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
    
    for line in grid:
        print(line)
    
    print("--------------")
    for cycle in range(1000000000):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "O":
                    offset = 1
                    while True:
                        if i-offset >= 0 and grid[i-offset][j] != "O" and grid[i-offset][j] != "#":
                            grid[i-offset][j] = "O"
                            grid[i-offset+1][j] = "."
                            grid[i][j] = "."
                            offset += 1
                        else:
                            break
        

    for line in grid:
        print(line)
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                total += len(grid) - i
        
    return total

def p2():


    return 0
        

print(p1())
print(p2())

