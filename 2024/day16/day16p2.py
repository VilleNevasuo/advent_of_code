import heapq

directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
turns = {"N": ("W", "E"), "E": ("N", "S"), "S": ("E", "W"), "W": ("S", "N")}

def p2(dict_map, start_pos, end_pos):
    direction_vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    start_state = (start_pos[0], start_pos[1], 1)
    
    dist = {start_state: 0}
    
    predecessors = {}
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_state))
    
    def add_predecessor(current_state, previous_state):
        if current_state not in predecessors:
            predecessors[current_state] = []
        predecessors[current_state].append(previous_state)
    
    while priority_queue:
        current_cost, (current_row, current_col, current_dir) = heapq.heappop(priority_queue)
        
        if current_cost > dist[(current_row, current_col, current_dir)]:
            continue
        
        forward_drow, forward_dcol = direction_vectors[current_dir]
        next_row, next_col = current_row + forward_drow, current_col + forward_dcol
        
        if (next_row, next_col) in dict_map and dict_map[(next_row, next_col)] != '#':
            forward_cost = current_cost + 1
            forward_state = (next_row, next_col, current_dir)
            
            if forward_state not in dist or forward_cost < dist[forward_state]:
                dist[forward_state] = forward_cost
                predecessors[forward_state] = [(current_row, current_col, current_dir)]
                heapq.heappush(priority_queue, (forward_cost, forward_state))
            elif forward_cost == dist[forward_state]:
                add_predecessor(forward_state, (current_row, current_col, current_dir))
        
        left_dir = (current_dir - 1) % 4
        turn_left_cost = current_cost + 1000
        left_state = (current_row, current_col, left_dir)
        
        if left_state not in dist or turn_left_cost < dist[left_state]:
            dist[left_state] = turn_left_cost
            predecessors[left_state] = [(current_row, current_col, current_dir)]
            heapq.heappush(priority_queue, (turn_left_cost, left_state))
        elif turn_left_cost == dist[left_state]:
            add_predecessor(left_state, (current_row, current_col, current_dir))
        
        right_dir = (current_dir + 1) % 4
        turn_right_cost = current_cost + 1000
        right_state = (current_row, current_col, right_dir)
        
        if right_state not in dist or turn_right_cost < dist[right_state]:
            dist[right_state] = turn_right_cost
            predecessors[right_state] = [(current_row, current_col, current_dir)]
            heapq.heappush(priority_queue, (turn_right_cost, right_state))
        elif turn_right_cost == dist[right_state]:
            add_predecessor(right_state, (current_row, current_col, current_dir))
    
    minimal_end_cost = None
    minimal_end_states = []
    for direction in range(4):
        end_state = (end_pos[0], end_pos[1], direction)
        if end_state in dist:
            end_cost = dist[end_state]
            if minimal_end_cost is None or end_cost < minimal_end_cost:
                minimal_end_cost = end_cost
                minimal_end_states = [end_state]
            elif end_cost == minimal_end_cost:
                minimal_end_states.append(end_state)
    
    tiles_on_minimal_paths = set()
    states_to_process = list(minimal_end_states)
    visited_states = set(minimal_end_states)
    
    while states_to_process:
        state = states_to_process.pop()
        (state_row, state_col, state_dir) = state
        
        tiles_on_minimal_paths.add((state_row, state_col))

        if state in predecessors:
            for pred_state in predecessors[state]:
                if pred_state not in visited_states:
                    visited_states.add(pred_state)
                    states_to_process.append(pred_state)
    return len(tiles_on_minimal_paths)

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


score = p2(dict_map,start,end)
print(score)


