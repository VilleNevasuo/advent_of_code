
import hashlib
i = 0

with open("input.txt") as file:
    for line in file:
        while True:

            line = "ckczppom" + str(i) 
            result = hashlib.md5(line.encode()).hexdigest()
            leading_chars = result[0:6]

            if leading_chars.count("0") == 6:
                print("yes")
                print(result)
                print(i)
                break
            i = i+1
            