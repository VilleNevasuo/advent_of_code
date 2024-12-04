

total_paper = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip().split("x")
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        shortest_path = min(length*2+width*2,length*2+height*2,width*2+height*2)
        
        total_paper += shortest_path + length*width*height

print(total_paper)  