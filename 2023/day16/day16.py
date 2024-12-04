

def create_beam(x,y, last_x, last_y, direction):
    return {'x': x, 'y': y, 'last_x': last_x, 'last_y': last_y, 'direction': direction}


def is_within_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def update_beam(beam, grid):
    x, y, last_x, last_y, direction = beam.values()
    current_cell = grid[x][y]
    new_beams = []
 
    if last_x == 0 and last_y == 0 and x == 0 and y == 0:
        direction = "right"
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



def p1():
    
    energized_tiles = set((0,0))
    iterations_without_new_tiles = 0
    max_iterations_without_new_tiles = 10
    print("-----------------------------")
    with open("input.txt") as file:
        grid = []
        for line in file:
            line = list(line.strip())
            grid.append(line)
        
        beams = [create_beam(0, 0, 0, 0, 'right')]
        while iterations_without_new_tiles < max_iterations_without_new_tiles:
            print("-----------------------------")
            print("energized tiles",energized_tiles)
            print("iterations without new tiles",iterations_without_new_tiles)

            tiles_visited_this_iteration = False
            new_beams = []
            for beam in beams:
                print("beam",beam)
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
        print(energized_tiles)
        return len(energized_tiles)
        

print(p1())
#print(p2())

