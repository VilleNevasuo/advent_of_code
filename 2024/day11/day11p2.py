with open("input.txt") as file:
    stones = file.readline().strip().split(" ")

def simulate_blinks(stone_counts):
    new_stone_counts = {}
    for stone, count in stone_counts.items():
        num = int(stone)
        if num == 0: 
            new_stone_counts["1"] = new_stone_counts.get("1", 0) + count
        elif len(stone) % 2 == 0: 
            mid = len(stone) // 2
            left = stone[:mid].lstrip("0") or "0"
            right = stone[mid:].lstrip("0") or "0"
            new_stone_counts[left] = new_stone_counts.get(left, 0) + count
            new_stone_counts[right] = new_stone_counts.get(right, 0) + count
        else: 
            transformed = str(num * 2024)
            new_stone_counts[transformed] = new_stone_counts.get(transformed, 0) + count
    return new_stone_counts

stone_counts = {stone: 1 for stone in stones}

for blink in range(75):
    stone_counts = simulate_blinks(stone_counts)

total_stones = sum(stone_counts.values())
print(stone_counts)
print(total_stones)
