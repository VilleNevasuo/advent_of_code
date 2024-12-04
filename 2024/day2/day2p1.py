



safe = 0 

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        line = list(map(int, line))
        
        increasing = False
        decreasing = False
        safe_report = True
        warning = 0
        
        for i in range(1, len(line)): 
            diff = abs(line[i] - line[i-1]) 
   
            if diff < 1 or diff > 3:
                warning += 1
                if warning > 1:
                    safe_report = False
                    break  
    
            if line[i] > line[i-1]:
                if decreasing == True:
                    warning += 1
                increasing = True
            elif line[i] < line[i-1]:
                if increasing ==True:
                    warning += 1
                decreasing = True

        if increasing and decreasing:
            safe_report = False

        if warning < 2:
            if safe_report:
                safe += 1
        

print(safe)


