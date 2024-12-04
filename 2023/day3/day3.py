

symbols = "~!@#$%^&*()_-+={[}|\:;'<,>?/"

def p1():

    legal_numbers = []
    grid = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            grid.append(line)

    numbers_indexes = []
    partnumber = ""
    for outer in range(len(grid)):
        for inner in range(len(grid[outer])):
            
            if grid[outer][inner].isdigit():
                partnumber = grid[outer][inner]
                numbers_indexes.append((inner,partnumber))
                partnumber = ""
            else:
                partnumber = ""
                legit = False
                
                for index, pair in enumerate(numbers_indexes):
                    check_index = pair[0]
                    #check up
                    if outer - 1 >= 0:
                        if grid[outer-1][check_index] in symbols:
                            legit = True
                            break
                    #check down
                    if outer + 1 < len(grid):
                        if grid[outer+1][check_index] in symbols:
                            legit = True
                            break
                    #check left
                    if check_index - 1 >= 0:
                        if grid[outer][check_index-1] in symbols:
                            legit = True
                            break
                    #check right
                    if check_index + 1 < len(grid[outer]):
                        if grid[outer][check_index + 1] in symbols:
                            legit = True
                            break
                    #check left diagonals if on leftmost endpoint
                    if index == 0:
                        if outer - 1 >= 0 and check_index - 1 >= 0:
                            if grid[outer-1][check_index-1] in symbols:
                                legit = True
                                break
                        if outer + 1 < len(grid) and check_index -1 >= 0:
                            if grid[outer+1][check_index-1] in symbols:
                                legit = True
                                break
                    #check right diagonals if on rightmost endpoint
                    if index == len(numbers_indexes)-1:
                        if outer -1 >= 0 and check_index + 1 < len(grid[outer]):
                            if grid[outer-1][check_index + 1] in symbols:
                                legit = True
                                break
                        if outer + 1 < len(grid) and check_index + 1 < len(grid[outer]):
                            if grid[outer+1][check_index+1] in symbols:
                                legit = True
                                break


                if legit:
                    subtotal = ""
                    for pair in numbers_indexes:
                       subtotal = subtotal + pair[1] 
                    legal_numbers.append(subtotal)


                numbers_indexes.clear()

        #start spaghetti
        if numbers_indexes:
            legit = False
                
            for index, pair in enumerate(numbers_indexes):
                check_index = pair[0]
                #check up
                if outer - 1 >= 0:
                    if grid[outer-1][check_index] in symbols:
                        legit = True
                        break
                #check down
                if outer + 1 < len(grid):
                    if grid[outer+1][check_index] in symbols:
                        legit = True
                        break
                #check left
                if check_index - 1 >= 0:
                    if grid[outer][check_index-1] in symbols:
                        legit = True
                        break
                #check right
                if check_index + 1 < len(grid[outer]):
                    if grid[outer][check_index + 1] in symbols:
                        legit = True
                        break
                #check left diagonals if on leftmost endpoint
                if index == 0:
                    if outer - 1 >= 0 and check_index - 1 >= 0:
                        if grid[outer-1][check_index-1] in symbols:
                            legit = True
                            break
                    if outer + 1 < len(grid) and check_index -1 >= 0:
                        if grid[outer+1][check_index-1] in symbols:
                            legit = True
                            break
                #check right diagonals if on rightmost endpoint
                if index == len(numbers_indexes)-1:
                    if outer -1 >= 0 and check_index + 1 < len(grid[outer]):
                        if grid[outer-1][check_index + 1] in symbols:
                            legit = True
                            break
                    if outer + 1 < len(grid) and check_index + 1 < len(grid[outer]):
                        if grid[outer+1][check_index+1] in symbols:
                            legit = True
                            break


            if legit:
                subtotal = ""
                for pair in numbers_indexes:
                    subtotal = subtotal + pair[1] 
                legal_numbers.append(subtotal)


            numbers_indexes.clear()
    
    print(legal_numbers)
    return sum(map(int,legal_numbers))




def p2():
    
    return 0


print(p1())
#print(p2())