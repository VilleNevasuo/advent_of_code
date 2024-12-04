
directions = [
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]


grid = []
with open("input.txt") as file:
     grid = [list(line.strip()) for line in file]

word = "MAS"
count = 0
word_length = len(word)

rows,cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            if all(
                0 <= r+k*dr < rows and
                0 <= c+k*dc < cols and 
                grid[r+k*dr][c+k*dc] == word[k]
                for k in range(word_length)
            ): 
                print(f"Found {word} starting at ({r}, {c}) in direction ({dr}, {dc})")
                
                #check nearby cells for x formation
                if dr == 1 and dc == 1: #word moving downright, check x formation moving upright
                    if grid[r+2][c] == 'M' and grid[r+1][c+1] == 'A' and grid[r][c+2] == 'S':
                        count += 1
                    elif grid[r+2][c] == 'S' and grid[r+1][c+1] == 'A' and grid[r][c+2] == 'M':
                        count += 1
                elif dr == -1 and dc == -1: #word moving upleft, check x formation moving downleft
                    if grid[r-2][c] == 'M' and grid[r-1][c-1] == 'A' and grid[r][c-2] == 'S':
                        count += 1
                    elif grid[r-2][c] == 'S' and grid[r-1][c-1] == 'A' and grid[r][c-2] == 'M':
                        count += 1
                elif dr == 1 and dc == -1: #word moving downleft, check x formation moving upleft
                    if grid[r+2][c] == 'M' and grid[r+1][c-1] == 'A' and grid[r][c-2] == 'S':
                        count += 1
                    elif grid[r+2][c] == 'S' and grid[r+1][c-1] == 'A' and grid[r][c-2] == 'M':
                        count += 1
                else: #word moving upright, check x formation moving
                    if grid[r-2][c] == 'M' and grid[r-1][c+1] == 'A' and grid[r][c+2] == 'S':
                        count += 1
                    elif grid[r-2][c] == 'S' and grid[r-1][c+1] == 'A' and grid[r][c+2] == 'M':
                        count += 1
print(count/2)