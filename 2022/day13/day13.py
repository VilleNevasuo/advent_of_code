

with open("test.txt", "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            packets.append(line)
        else:
            print(packets[0])
            print(packets[1])
            if compare(packets[0], packets[1]):
                total += 1
            packets = []
            
print("asd")
print(packets)
            