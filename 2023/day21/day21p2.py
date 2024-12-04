
from collections import deque

def bfs_explore_garden_include_start(map_grid, start_x, start_y, steps):
    # Directions for moving: north, south, east, west
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Queue for BFS, each element is a tuple (x, y, current_step)
    queue = deque([(start_x, start_y, 0)])

    # Set to store visited garden plots with steps
    visited = set()

    while queue:
        x, y, current_step = queue.popleft()

        # If we've already visited this cell with equal or fewer steps, skip it
        if (x, y, current_step) in visited:
            continue

        # Add the current cell to visited
        visited.add((x, y, current_step))

        # Stop if we have reached the desired number of steps
        if current_step == steps:
            continue

        # Explore adjacent cells
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check bounds and if it's a garden plot or the starting position
            if 0 <= new_x < len(map_grid) and 0 <= new_y < len(map_grid[0]) and (map_grid[new_x][new_y] == '.' or (new_x == start_x and new_y == start_y)):
                queue.append((new_x, new_y, current_step + 1))

    # Count the number of unique garden plots that can be reached in exactly the given number of steps, including the starting position
    return len({(x, y) for x, y, step in visited if step == steps})

# Count the reachable plots in the example (for 6 steps), including the starting position

with open("input.txt") as file:
    map_grid = [[line for line in line.strip()] for line in file if line.strip()]

for i in range(len(map_grid)):
    for j in range(len(map_grid)):
        if map_grid[i][j] == "S":
            start_x = i
            start_y = j

print(bfs_explore_garden_include_start(map_grid, start_x, start_y, 64))  # Expecting 16 for the example input with 6 steps
