
def is_corner(x, y, grid):
    return (x == 0 or x == len(grid) - 1) and (y == 0 or y == len(grid[0]) - 1)

def get_edge_points(grid):
    top_edge = [(0, y) for y in range(len(grid[0]))]
    bottom_edge = [(len(grid) - 1, y) for y in range(len(grid[0]))]
    left_edge = [(x, 0) for x in range(1, len(grid) - 1)]
    right_edge = [(x, len(grid[0]) - 1) for x in range(1, len(grid) - 1)]
    return top_edge + bottom_edge + left_edge + right_edge

def initial_directions(x, y, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    if x == 0 and y == 0:
        return ['down', 'right']
    elif x == 0 and y == grid_width - 1:
        return ['down', 'left']
    elif x == grid_height - 1 and y == 0:
        return ['up', 'right']
    elif x == grid_height - 1 and y == grid_width - 1:
        return ['up', 'left']
    else:
        if x == 0: return ['down']
        elif x == grid_height - 1: return ['up']
        elif y == 0: return ['right']
        else: return ['left']

def create_beam(x,y, last_x, last_y, direction):
    return {'x': x, 'y': y, 'last_x': last_x, 'last_y': last_y, 'direction': direction}


def is_within_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def update_beam(beam, grid):
    x, y, last_x, last_y, direction = beam.values()
    current_cell = grid[x][y]
    new_beams = []
    
    if last_x == x and last_y == y:
        direction = direction
    elif y > last_y:
        direction = "right"
    elif y < last_y:
        direction = "left"
    elif x > last_x:
        direction = "down"
    else:
        direction = "up"

    last_x = x
    last_y = y
    if current_cell == "/":
        if direction == "right":
            direction = "up"
            x -= 1
        elif direction == "left":
            direction = "down"
            x += 1
        elif direction == "down":
            y -= 1
            direction = "left"
        else:
            direction = "right"
            y += 1
    elif current_cell == "\\":
        if direction == "right":
            direction = "down"
            x += 1
        elif direction == "left":
            direction = "up"
            x -= 1
        elif direction == "down":
            direction = "right"
            y += 1
        else:
            direction = "left"
            y -= 1

    elif current_cell == '|':
        if direction == "right" or direction == "left":
            return [create_beam(x-1, y, x, y, 'up'), create_beam(x+1, y, x, y, 'down')]
        elif direction == "up":
            x -= 1
        else:
            x += 1
    elif current_cell == '-':
        if direction == "up" or direction == "down":
            return [create_beam(x, y-1, x, y, 'left'), create_beam(x, y+1, x, y, 'right')]
        elif direction == "right":
            y += 1
        else:
            y -= 1
    else:
        if direction == "up":
            x -= 1
        elif direction == "down":
            x += 1
        elif direction == "right":
            y += 1
        else:
            y -= 1

    return [{'x': x, 'y': y, 'last_x': last_x, 'last_y': last_y, 'direction': direction}]



def process_grid_from_point(grid,x,y,direction):
    
    energized_tiles = set((x,y))
    iterations_without_new_tiles = 0
    max_iterations_without_new_tiles = 4
    print("-----------------------------")
    
    beams = [create_beam(x, y, x, y, direction)]
    while iterations_without_new_tiles < max_iterations_without_new_tiles:

        tiles_visited_this_iteration = False
        new_beams = []
        for beam in beams:
            updated_beams = update_beam(beam,grid)
    
            for ub in updated_beams:
                
                if not is_within_bounds(ub['x'], ub['y'], grid):
                    continue
                if (ub['x'], ub['y']) not in energized_tiles:
                    energized_tiles.add((ub['x'], ub['y']))
                    tiles_visited_this_iteration = True
                new_beams.extend([ub])

        if not tiles_visited_this_iteration:
            iterations_without_new_tiles += 1
        else:
            iterations_without_new_tiles = 0

            
        beams = new_beams
    return len(energized_tiles)
    

def find_best_starting_point(grid):
    edge_points = get_edge_points(grid)
    best_start = None
    max_energized = 0
    
    for x, y in edge_points:
        directions = initial_directions(x, y, grid)
        for direction in directions:
            energized_tiles = process_grid_from_point(grid, x, y, direction)
            if energized_tiles > max_energized:
                max_energized = energized_tiles
                best_start = (x, y, direction)
        print(x,y, energized_tiles, max_energized)

    return best_start, max_energized


with open("input.txt") as file:
    grid = []
    for line in file:
        line = list(line.strip())
        grid.append(line)
print(find_best_starting_point(grid))
maxsofar = 7696

