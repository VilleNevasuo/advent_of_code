from collections import deque

directions = {"UP" : (-1,0), "DOWN" : (1,0), "LEFT" : (0,-1), "RIGHT" : (0,1)}

def bfs(start,end, dict_map):

    steps = 0
    queue = deque([(start,steps)])
    visited = set()

    while queue:
        current, steps = queue.popleft()
        if current in visited:
            continue
            
        visited.add(current)

        if current == end:
            print("at the end")
            return steps
        
        for dir in directions.values():
            dy,dx = dir
            new_pos = (current[0]+dy, current[1]+dx)
            if 0 <= new_pos[0] < 71 and 0 <= new_pos[1] < 71:
                if dict_map[new_pos] != "#" and new_pos not in visited:
                    queue.append((new_pos,steps+1))
         
    return -1


dict_map = {}
for i in range(71):
    for j in range(71):
        dict_map[(i,j)] = "."

with open("input.txt") as file:
    for i, line in enumerate(file):
        if i >= 1024:
            break
        line = line.strip().split(",")
        y,x = int(line[1]),int(line[0])
        dict_map[(y,x)] = "#"

start = (0,0)
end = (70,70)


min_steps = bfs(start,end,dict_map)

print(min_steps)

        