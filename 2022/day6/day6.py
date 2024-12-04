
markers = []

with open("data.txt", "r") as file:
    s = file.read()
    for index, char in enumerate(s.strip()):
        markers.append(char)
        if len(markers) == 4:
            if len(markers) == len(set(markers)):
                print(index+1, markers)
                quit()
            del markers[0]
