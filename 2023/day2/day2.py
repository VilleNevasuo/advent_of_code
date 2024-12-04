

def p1():

    quota = [12,13,14] #rgb
    total = 0
    with open("input.txt") as file:
        for index, line in enumerate(file):
            game_legit = True
            line = line.split(":")
            line = line[1]
            game = line.split(";")
            for iteration in game:
                r = 0
                g = 0
                b = 0
                iteration = iteration.strip()
                iteration = iteration.split(",")
                
                for cubes in iteration:
                    cubes = cubes.strip()
                    cubes = cubes.split(" ")
                    if cubes[1] == "red":
                        r += int(cubes[0])
                    elif cubes[1] == "green":
                        g += int(cubes[0])
                    else:
                        b += int(cubes[0])
                if r > quota[0] or g > quota[1] or b > quota[2]:
                    game_legit = False
                    break
                    
            if game_legit:
                total += index + 1
            

    return total


def p2():
    
    total = 0
    with open("input.txt") as file:
        for index, line in enumerate(file):
            highest_red = 0
            highest_green = 0
            highest_blue = 0
            line = line.split(":")
            line = line[1]
            game = line.split(";")
            for iteration in game:
                iteration = iteration.strip()
                iteration = iteration.split(",")
                
                for cubes in iteration:
                    cubes = cubes.strip()
                    cubes = cubes.split(" ")
                    if cubes[1] == "red":
                        if int(cubes[0]) > highest_red:
                            highest_red = int(cubes[0])
                    elif cubes[1] == "green":
                        if int(cubes[0]) > highest_green:
                            highest_green = int(cubes[0])
                    else:
                        if int(cubes[0]) > highest_blue:
                            highest_blue = int(cubes[0])
                
            power = highest_blue*highest_green*highest_red
            print(power)
            total += power
                
            
    return total


print(p1())
print(p2())