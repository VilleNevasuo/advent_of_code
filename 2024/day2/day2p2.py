def is_safe(levels):
    if len(levels) < 2:
        return False 

    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    if any(diff == 0 for diff in diffs):
        return False

    if all(1 <= diff <= 3 for diff in diffs):
        return True 

    if all(-3 <= diff <= -1 for diff in diffs):
        return True 

    return False

with open('input.txt', 'r') as file:
    lines = file.readlines()

safe_reports = 0

for line in lines:
    line = line.strip()
    if not line:
        continue 
    levels = [int(x) for x in line.split()]

    if is_safe(levels):
        safe_reports += 1
    else:
        for i in range(len(levels)):
            levels_removed = levels[:i] + levels[i+1:]
            if len(levels_removed) >= 2 and is_safe(levels_removed):
                safe_reports += 1
                break  

print("asd")
print(safe_reports)
