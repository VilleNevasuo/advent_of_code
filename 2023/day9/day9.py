from collections import Counter



def p1():

    masterlist = []
    total = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            masterlist.append(line)
    
    for list in masterlist:
        history = []
        historysublist = list
        history.append(historysublist)
        while True:
            values = []
            for i in range(len(historysublist)):
                if i < len(historysublist)-1:
                    diff = int(historysublist[i+1]) - int(historysublist[i])
                    values.append(diff)
            history.append(values)
            historysublist = values
            if historysublist.count(0) == len(historysublist):
                break
        
        for i, list in enumerate(reversed(history)):
            if i == 0:
                list.append(0)
            else:
                value_to_left = int(list[-1])
                value_below = int(history[-i][-1])
                list.append(value_to_left+value_below)
        
        to_add = history[0][-1]
        total += to_add
    
        
    return total
        


def p2():

    masterlist = []
    total = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            masterlist.append(line)
    
    for list in masterlist:
        history = []
        historysublist = list
        history.append(historysublist)
        while True:
            values = []
            for i in range(len(historysublist)):
                if i < len(historysublist)-1:
                    diff = int(historysublist[i+1]) - int(historysublist[i])
                    values.append(diff)
            history.append(values)
            historysublist = values
            if historysublist.count(0) == len(historysublist):
                break
        
        for i, list in enumerate(reversed(history)):
            if i == 0:
                list.insert(0,0)
            else:
                value_to_right = int(list[0])
                value_below = int(history[-i][0])
                list.insert(0,value_to_right-value_below)
        
        to_add = history[0][0]
        total += int(to_add)
        
    
        
    return total

print(p1())
print(p2())

