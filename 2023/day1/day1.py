
import re

texts = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ints = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def p1():

    with open("input.txt") as file:
        sum = 0
        for line in file:
            for char in line:
                if char.isdigit():
                    first = char
                    break
            for char in reversed(line):
                if char.isdigit():
                    last = char
                    break
            fin = first + last
            sum += int(fin)
        return sum

def p2():

    l = []
    sum = 0
    with open("input.txt") as file:
        for line in file:
            indexes = {}
            for written, number in zip(texts, ints):
                if written in line:
                    first_index = line.find(written)
                    last_index = line.rfind(written)
                    if first_index == last_index:
                        indexes[line.find(written)] = written
                    else:
                        indexes[line.find(written)] = written
                        indexes[line.rfind(written)] = written
                if number in line:
                    first_index = line.find(number)
                    last_index = line.rfind(number)

                    if first_index == last_index:
                        indexes[line.find(number)] = number
                    else:
                        indexes[line.find(number)] = number
                        indexes[line.rfind(number)] = number

            lowest_index = min(indexes.keys())
            highest_index = max(indexes.keys())

            lowest_number = indexes[lowest_index]
            highest_number = indexes[highest_index]

            if not len(indexes[lowest_index]) == 1:
                lowest_number = mapping.get(indexes[lowest_index])
            if not len(indexes[highest_index]) == 1:
                highest_number = mapping.get(indexes[highest_index])

            fin = str(lowest_number) + str(highest_number)

            sum += int(fin)

        return sum


print(p1())
print(p2())
