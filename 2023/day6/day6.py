


def p1():

    ways_to_win = []
    races = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            
            if "Time" in line:
                line = line.split(":")
                times = line[1].strip().split(" ")
                while("" in times):
                    times.remove("")
            else:
                line = line.split(":")
                distances = line[1].strip().split(" ")
                while("" in distances):
                    distances.remove("")
                
    for time, dist in zip(times,distances):
        races.append((time,dist))
    
    for race in races:
        winning_holds = []
        time, my_dist = int(race[0]), int(race[1])
        dist_to_beat = int(race[1]) 
        
        for hold in range(time):
            if hold == 0:
                continue
            time_left = time
            time_left -= hold
            dist_travelled = hold * time_left
            if dist_travelled > dist_to_beat:
                winning_holds.append(hold)

        ways_to_win.append(len(winning_holds))
    
    total = ways_to_win[0]
    for i in range(len(ways_to_win)):
        if i == 0:
            continue
        total = total * ways_to_win[i]
    
    return total
    



def p2():

    ways_to_win = []
    races = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            
            if "Time" in line:
                line = line.split(":")
                times = line[1].strip().split(" ")
                while("" in times):
                    times.remove("")
            else:
                line = line.split(":")
                distances = line[1].strip().split(" ")
                while("" in distances):
                    distances.remove("")
    
    racetime = "".join(times)
    distance = "".join(distances)


    race = (racetime, distance)


    winning_holds = []
    time, my_dist = int(race[0]), int(race[1])
    dist_to_beat = int(race[1]) 
    
    for hold in range(time):
        if hold == 0:
            continue
        time_left = time
        time_left -= hold
        dist_travelled = hold * time_left
        if dist_travelled > dist_to_beat:
            winning_holds.append(hold)

    ways_to_win.append(len(winning_holds))
    
    total = ways_to_win[0]
    for i in range(len(ways_to_win)):
        if i == 0:
            continue
        total = total * ways_to_win[i]
    
    return total
    



print(p1())
print(p2())
