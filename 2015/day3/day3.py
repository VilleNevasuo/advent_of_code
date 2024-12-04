


houses_visited = set()
santa_house = (0,0)
robo_house = (0,0)
current_x = 0
current_y = 0
robo_x = 0
robo_y = 0

houses_visited.add(santa_house)

moves = {"^" : (0,1), "v" : (0,-1), ">" : (1,0), "<" : (-1,0)}

with open("input.txt") as file:
    for directions in file:
        for i, direction in enumerate(directions):
            
            if i % 2 == 0:
                dx,dy = moves[direction]
                current_x, current_y = current_x + dx, current_y + dy

                houses_visited.add((current_x,current_y))
            else:
                dx,dy = moves[direction]
                robo_x, robo_y = robo_x + dx, robo_y + dy

                houses_visited.add((robo_x,robo_y))
    print(len(houses_visited))




