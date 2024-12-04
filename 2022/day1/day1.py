<<<<<<< HEAD


sum = 0
total_calories = []

with open('data.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            total_calories.append(sum)
            sum = 0
        else:
            sum = sum + int(line.strip())

total_calories.sort()

print(max(total_calories))
print(total_calories[-1]+total_calories[-2]+total_calories[-3])


# with open('data.txt', 'r') as file:
#     data = file.read()

# x = sorted(sum(map(int, x.split())) for x in data.split("\n\n"))

# print(x)
=======


sum = 0
total_calories = []

with open('data.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            total_calories.append(sum)
            sum = 0
        else:
            sum = sum + int(line.strip())

total_calories.sort()

print(max(total_calories))
print(total_calories[-1]+total_calories[-2]+total_calories[-3])


# with open('data.txt', 'r') as file:
#     data = file.read()

# x = sorted(sum(map(int, x.split())) for x in data.split("\n\n"))

# print(x)
>>>>>>> e481f32ca53b50252269e71134bdc26e3879ff2a
