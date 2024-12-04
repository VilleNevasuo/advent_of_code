from collections import Counter

from math import gcd

def p1():

    start = "AAA"
    end = "ZZZ"
    current = "AAA"
    steps = 0

    desert_map = {}
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) < 1:
                continue
            if "=" not in line:
                directions = line
            else:
                line = line.split("=")
                line[0] = line[0].strip()
                line[1] = line[1].strip()
                line[1] = line[1].strip("()").split(",")
                line[1][1] = line[1][1].strip()
                desert_map[line[0]] = line[1]

    while current != end:
        for direction in directions:
            values = desert_map[current]
            if direction == "R":
                current = values[1]
            else:
                current = values[0]
            steps += 1
    
    return steps

def lcm(x, y):
    return x * y // gcd(x, y)

def find_path_length(desert_map, directions, start_node):
    current_node = start_node
    steps = 0

    while not current_node.endswith('Z'):
        direction = directions[steps % len(directions)]
        current_node = desert_map[current_node][0] if direction == 'L' else desert_map[current_node][1]
        steps += 1

    return steps

def p2():

    current = "AAA"
    steps = 0

    desert_map = {}
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) < 1:
                continue
            if "=" not in line:
                directions = line
            else:
                line = line.split("=")
                line[0] = line[0].strip()
                line[1] = line[1].strip()
                line[1] = line[1].strip("()").split(",")
                line[1][1] = line[1][1].strip()
                desert_map[line[0]] = line[1]

    start_nodes = [node for node in desert_map if node.endswith('A')]
    path_lengths = [find_path_length(desert_map, directions, node) for node in start_nodes]


    total_steps = path_lengths[0]
    for length in path_lengths[1:]:
        total_steps = lcm(total_steps, length)

    return total_steps


print(p1())
print(p2())

