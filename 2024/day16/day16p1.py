from heapq import heappop, heappush

DIRECTIONS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

TURNS = {"N": ("W", "E"), "E": ("N", "S"), "S": ("E", "W"), "W": ("S", "N")}

def p1(dict_map, start, end):
    pq = [(0, (start, "E"))]
    visited = {}

    while pq:
        score, ((y, x), direction) = heappop(pq)

        if (y, x) == end:
            return score

        if ((y, x), direction) in visited and visited[((y, x), direction)] <= score:
            continue
        visited[((y, x), direction)] = score


        dy, dx = DIRECTIONS[direction]
        new_pos = (y + dy, x + dx)
        if dict_map.get(new_pos, '#') != '#':
            heappush(pq, (score + 1, (new_pos, direction)))


        for new_dir in TURNS[direction]:
            heappush(pq, (score + 1000, ((y, x), new_dir)))

    return float('inf')  


dict_map = {}
with open("input.txt") as file:
    for y, line in enumerate(file):
        line = line.strip()
        for x, el in enumerate(line):
            if el == "S":
                start = (y, x)
            if el == "E":
                end = (y, x)
            dict_map[(y, x)] = el

score = p1(dict_map, start, end)
print(score)
