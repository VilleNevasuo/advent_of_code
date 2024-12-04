import heapq

def read_grid_from_file():
    with open("input.txt", 'r') as file:
        return [[int(char) for char in line.strip()] for line in file if line.strip()]

def min_heat_loss(grid):
    rows, cols = len(grid), len(grid[0])
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    dir_list = list(directions.keys())

    def create_graph():
        graph = {}
        for r in range(rows):
            for c in range(cols):
                for dir in directions:
                    for steps in range(1, 4):  # Steps can be 1, 2, or 3
                        node = (r, c, dir, steps)
                        graph[node] = []
        return graph
    def connect_graph(graph):
        
        for r in range(rows):
            for c in range(cols):
                for i, dir in enumerate(dir_list):
                    for steps in range(1, 4):
                        current_node = (r, c, dir, steps)
                        dr, dc = directions[dir]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            # Connect to the next block in the same direction
                            if steps < 3:  # Can continue in the same direction
                                next_node = (nr, nc, dir, steps + 1)
                                graph[current_node].append((next_node, int(grid[nr][nc])))
                            # Connect to adjacent directions (left and right turns)
                            for j in [-1, 1]:
                                next_dir = dir_list[(i + j) % 4]
                                next_node = (nr, nc, next_dir, 1)
                                graph[current_node].append((next_node, int(grid[nr][nc])))
        
    def dijkstra(graph, start, end):
        heap = [(0, start)]
        heat_loss_to_node = {node: float('inf') for node in graph}
        heat_loss_to_node[start] = 0
        while heap:
            current_heat_loss, current_node = heapq.heappop(heap)
            if current_heat_loss > heat_loss_to_node[current_node]:
                continue
            for neighbour, additional_heat in graph[current_node]:
                new_heat_loss = current_heat_loss + additional_heat
                if new_heat_loss < heat_loss_to_node[neighbour]:
                    heat_loss_to_node[neighbour] = new_heat_loss
                    heapq.heappush(heap, (new_heat_loss, neighbour))
        return heat_loss_to_node[end]

    graph = create_graph()
    connect_graph(graph)

    start_nodes = [(0, 0, dir, 1) for dir in directions]
    end_nodes = [(rows - 1, cols - 1, dir, steps) for dir in directions for steps in range(1, 4)]
    
    return min(dijkstra(graph, start, end) for start in start_nodes for end in end_nodes)

grid = read_grid_from_file()
print(min_heat_loss(grid))
