from itertools import product

with open("input.txt") as file:
    for line in file:
        elements = []
        totals = []
        subtotal = 0
        line = line.strip().split(" ")
        test_value = line[0][:-1]
        for el in line[1:]:
            elements.append(el)
        combinations = 2**(len(elements)-1)
        n = len(elements)

        print(line)
        
        operator_combinations = list(product('+-*', repeat=n-1))

        for operators in operator_combinations:
            result = elements[0]
            expression = str(elements[0]) 
            for idx, operator in enumerate(operators):
                if operator == '+':
                    result += elements[idx + 1]
                elif operator == '*':
                    result *= elements[idx + 1]
                expression += f" {operator} {elements[idx + 1]}"
            print(f"{expression} = {result}")
