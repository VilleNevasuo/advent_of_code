
grid_dict = {}

with open("input.txt") as file:
    for y, line in enumerate(file):
        line = line.rstrip("\n")
        for x, char in enumerate(line):
            grid_dict[(y, x)] = char


start = None
for coord, val in grid_dict.items():
    if val == '^':
        start = coord
        break

current = start
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
direction_order = ['^', '>', 'v', '<'] 
visited = set()
marker = val

def get_next_marker(marker):
    idx = (direction_order.index(marker) + 1) % len(direction_order)
    return direction_order[idx]

while True:
        visited.add(current)
        dx,dy = directions[marker]
        new_position = (current[0]+dx, current[1]+dy)
        if new_position in grid_dict:
            if grid_dict[new_position] == "#":
                marker = get_next_marker(marker)
            else:
                grid_dict[current] = '.'
                grid_dict[new_position] = marker
                current = new_position
                print(current)
        else:
            print("out of bounds")
            break
    

print(len(visited))

