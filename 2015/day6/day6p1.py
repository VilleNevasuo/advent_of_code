

nodes = [[0 for x in range(1000)] for j in range(1000)]


with open("input.txt") as file:
    for line in file:
        
        line = line.strip().split(" ")
        
        last_coordinate = line[-1]
        
        if line[0] == "turn":
            first_coordinate = line[2]
            command = line[0] + line[1]
        else:
            first_coordinate = line[1]
            command = line[0]

        first_coordinate = first_coordinate.split(",")
        last_coordinate = last_coordinate.split(",")
        
        start_x = int(first_coordinate[0])
        start_y = int(first_coordinate[1])

        end_x = int(last_coordinate[0])
        end_y = int(last_coordinate[1])

        if command == "toggle":
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    nodes[i][j] ^= 1
        elif command == "turnon":
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    nodes[i][j] = 1
        else:
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    nodes[i][j] = 0
            
nodes_on = 0
for node in nodes:
    nodes_on += node.count(1)

print(nodes_on)