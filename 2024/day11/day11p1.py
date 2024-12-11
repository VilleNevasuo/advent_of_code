with open("input.txt") as file:
    stones = file.readline().strip().split(" ")

def simulate_blink(stones):
    next_stones = []
    for stone in stones:
        num = int(stone)
        
        if num == 0:
            next_stones.append("1")
        
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid].lstrip("0") or "0" 
            right = stone[mid:].lstrip("0") or "0"
            next_stones.extend([left, right])
        
        else:
            next_stones.append(str(num * 2024))
    
    return next_stones

for blink in range(75):
    stones = simulate_blink(stones)

print(len(stones))
