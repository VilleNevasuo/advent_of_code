def read_grid(filename):
    grid_dict = {}
    with open(filename) as file:
        for y, line in enumerate(file):
            line = line.rstrip("\n")
            for x, char in enumerate(line):
                grid_dict[(y, x)] = char
    return grid_dict

def find_start(grid_dict):
    for coord, val in grid_dict.items():
        if val == '^':
            return coord, val
    return None, None

def get_next_marker(marker):
    direction_order = ['^', '>', 'v', '<']
    idx = (direction_order.index(marker) + 1) % len(direction_order)
    return direction_order[idx]

def run_simulation(grid_dict, start, start_marker):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    
    current = start
    marker = start_marker

    seen_states = set()

    while True:
        state = (current[0], current[1], marker)
        if state in seen_states:
            return "loop"
        seen_states.add(state)
        
        dx, dy = directions[marker]
        new_position = (current[0] + dx, current[1] + dy)

        if new_position in grid_dict:
            if grid_dict[new_position] == "#":
                marker = get_next_marker(marker)
            else:
                current = new_position
        else:
            return "out_of_bounds"

def count_loops(grid_dict):
    start, start_marker = find_start(grid_dict)

    valid_positions = [
        pos for pos, val in grid_dict.items()
        if val not in '#^>v<' and pos != start
    ]

    loop_count = 0

    for pos in valid_positions:
        original_val = grid_dict[pos]
        grid_dict[pos] = '#'

        result = run_simulation(grid_dict, start, start_marker)
        if result == "loop":
            loop_count += 1

        grid_dict[pos] = original_val

    return loop_count



grid_dict = read_grid("input.txt")
result = count_loops(grid_dict)
print(result)
