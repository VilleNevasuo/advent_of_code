
from collections import deque

def calculate_cost(garden):
    visited = set()
    total_cost = 0

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        plant_type = garden[start]
        area = 0
        perimeter = 0

        while queue:
            print(queue)
            y, x = queue.popleft()
            area += 1

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if (ny, nx) in garden:
                    if garden[(ny, nx)] == plant_type and (ny, nx) not in visited:
                        queue.append((ny, nx))
                        visited.add((ny, nx))
                    elif garden[(ny, nx)] != plant_type:
                        perimeter += 1
                else:
                    #out of bounds 
                    perimeter += 1

        return area, perimeter

    for coord in garden:
        if coord not in visited:
            area, perimeter = bfs(coord)
            total_cost += area * perimeter

    return total_cost

garden = {}
with open("input.txt") as file:
    for y, garden_line in enumerate(file):
        garden_line = garden_line.strip()
        for x, plant in enumerate(garden_line):
            garden[(y, x)] = plant

total_cost = calculate_cost(garden)
print(total_cost)