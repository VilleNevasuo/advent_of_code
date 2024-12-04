
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]



grid = []
with open("input.txt") as file:
     grid = [list(line.strip()) for line in file]

word = "XMAS"
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
                count += 1

print(count)