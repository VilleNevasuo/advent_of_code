import copy


def take_step(step):

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze_comp[i][j] == step:
                if i > 0 and maze_comp[i-1][j] == 0 and maze[i][j] - maze[i-1][j] > -2:
                    maze_comp[i-1][j] = step + 1
                if j > 0 and maze_comp[i][j-1] == 0 and maze[i][j] - maze[i][j-1] > -2:
                    maze_comp[i][j-1] = step + 1
                if i < len(maze)-1 and maze_comp[i+1][j] == 0 and maze[i][j] - maze[i+1][j] > -2:
                    maze_comp[i+1][j] = step + 1
                if j < len(maze[0])-1 and maze_comp[i][j+1] == 0 and maze[i][j] - maze[i][j+1] > -2:
                    maze_comp[i][j+1] = step + 1


maze = []
maze_comp = []


with open("data.txt", "r") as file:
    for line in file:
        l = []
        line = line.strip()
        for char in line:
            l.append(char)
        maze.append(l)


for i in range(len(maze)):
    l = []
    for a in range(len(maze[0])):
        if maze[i][a] == "S":
            maze[i][a] = 1
            starts = i, a
        elif maze[i][a] == "a":
            maze[i][a] = ord("a") - 96
        elif maze[i][a] == "E":
            end = i, a
            maze[i][a] = ord("z") - 96
        else:
            maze[i][a] = ord(maze[i][a]) - 96
        l.append(0)
    maze_comp.append(l)

maze_comp[starts[0]][starts[1]] = 1


k = 0
maze_comp[starts[0]][starts[1]] = 1
while maze_comp[end[0]][end[1]] == 0:
    k += 1
    take_step(k)


print(maze_comp[end[0]][end[1]]-1)
