from collections import Counter



def p1():

    rows = []
    total = 0
    columns_to_sum = 0
    rows_to_sum = 0
    
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line = list(line)
            if len(line) == 0:
                columns = [list(column) for column in zip(*rows)]
                for i in range(len(rows)):
                    if i+1 < len(rows):
                        if rows[i] == rows[i+1]:
                            symmetric = True
                            for j in range(1,len(rows)//2 +1):
                                if i-j >= 0 and i+j+1 < len(rows):
                                    if rows[i-j] != rows[i+j+1]:
                                        symmetric = False
                                        break
                            if symmetric:
                                rows_to_sum += i + 1
                        
                for i in range(len(columns)):
                    if i+1 < len(columns):
                        if columns[i] == columns[i+1]:
                            symmetric = True
                            for j in range(1, len(columns)//2 +1):
                                if i-j >= 0 and i+j+1 < len(columns):
                                    if columns[i-j] != columns[i+j+1]:
                                        symmetric = False
                                        break
                            if symmetric:
                                columns_to_sum += i + 1
                
                columns = []
                rows = []
            else:
                rows.append(line)
    total = columns_to_sum + rows_to_sum*100
    return total
        


def p2():


    rows = []
    total = 0
    found_new = False
    
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line = list(line)
            if len(line) == 0:
                found_new = False
                copied_rows = [row[:] for row in rows]
                for outer in range(len(rows)):
                    if found_new:
                        break
                    for inner in range(len(rows[outer])):
                        rows = [row[:] for row in copied_rows]
                        if rows[outer][inner] == ".":
                            rows[outer][inner] = "#"
                        else:
                            rows[outer][inner] = "."

                        columns_to_sum = 0
                        og_columns_to_sum = 0
                        rows_to_sum = 0
                        og_rows_to_sum = 0

                        copied_columns = [list(column) for column in zip(*copied_rows)]
                        columns = [list(column) for column in zip(*rows)]

                        for i in range(len(copied_rows)):
                            if i+1 < len(copied_rows):
                                if copied_rows[i] == copied_rows[i+1]:
                                    symmetric = True
                                    for j in range(1,len(copied_rows)//2 +1):
                                        if i-j >= 0 and i+j+1 < len(copied_rows):
                                            if copied_rows[i-j] != copied_rows[i+j+1]:
                                                symmetric = False
                                                break
                                    if symmetric:
                                        og_rows_to_sum = i + 1    

                        for i in range(len(rows)):
                            if i+1 < len(rows):
                                if rows[i] == rows[i+1]:
                                    symmetric = True
                                    for j in range(1,len(rows)//2 +1):
                                        if i-j >= 0 and i+j+1 < len(rows):
                                            if rows[i-j] != rows[i+j+1]:
                                                symmetric = False
                                                break
                                    if symmetric:
                                        rows_to_sum = i + 1    
                        

                        for i in range(len(columns)):
                            if i+1 < len(columns):
                                if columns[i] == columns[i+1]:
                                    symmetric = True
                                    for j in range(1, len(columns)//2 +1):
                                        if i-j >= 0 and i+j+1 < len(columns):
                                            if columns[i-j] != columns[i+j+1]:
                                                symmetric = False
                                                break
                                    if symmetric:
                                        columns_to_sum = i + 1

                        for i in range(len(copied_columns)):
                            if i+1 < len(copied_columns):
                                if copied_columns[i] == copied_columns[i+1]:
                                    symmetric = True
                                    for j in range(1, len(copied_columns)//2 +1):
                                        if i-j >= 0 and i+j+1 < len(copied_columns):
                                            if copied_columns[i-j] != copied_columns[i+j+1]:
                                                symmetric = False
                                                break
                                    if symmetric:
                                        og_columns_to_sum = i + 1

                        if columns_to_sum > 0 and og_columns_to_sum != columns_to_sum:
                            total = total + columns_to_sum + rows_to_sum*100
                            found_new = True
                            break


                        if rows_to_sum > 0 and og_rows_to_sum != rows_to_sum:
                            total = total + columns_to_sum + rows_to_sum*100
                            found_new = True
                            break
                columns = []
                rows = []
                print("rows", og_rows_to_sum, rows_to_sum)
                print("columns", og_columns_to_sum, columns_to_sum)
            else:
                rows.append(line)

    
    print(columns_to_sum, rows_to_sum)
    return total
        

print(p1())
print(p2())

