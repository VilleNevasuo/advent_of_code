import numpy as np


def compare_trees(strip, current_tree, i, direction, scorecheck=0):

    score = 0
    if direction == "west":
        strip = strip[0:i]
        strip = strip[::-1]
        for tree in strip:
            if tree >= current_tree:
                if scorecheck == 1:
                    return score+1
                return False
            score += 1
        if scorecheck == 1:
            return score
        return True
    else:
        for tree in strip[i+1:]:
            if tree >= current_tree:
                if scorecheck == 1:
                    return score+1
                return False
            score += 1
        if scorecheck == 1:
            return score
        return True


visible = 0
grid = []
npgrid = []
gridt = []
scenic_score = []


with open("data.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

        l = []
        l[:0] = line.strip()
        npgrid.append(l)

visible += (len(grid)*4) - 4

print("initially visible", visible)

arr1 = np.array(npgrid)
arrt1 = arr1.transpose()
npgrid = arrt1.tolist()

for el in npgrid:
    s = "".join(el)
    gridt.append(s)

print(grid)
print(gridt)

for strip in range(len(grid)):
    if strip == 0 or strip == len(grid)-1:
        continue
    for tree in range(len(grid[0])):
        if tree == 0 or tree == len(grid[0])-1:
            continue

        strip_norm = grid[strip]
        strip_tran = gridt[tree]
        current_tree_norm = grid[strip][tree]
        current_tree_tran = gridt[tree][strip]
        tree_norm = tree
        tree_tran = strip

        if compare_trees(strip_norm, current_tree_norm, tree_norm, "west"):
            print("west normal visible")
            visible += 1

        elif compare_trees(strip_norm, current_tree_norm, tree_norm, "east"):
            print("east normal visible")
            visible += 1

        elif compare_trees(strip_tran, current_tree_tran, tree_tran, "west"):
            print("west transpose visible")
            visible += 1

        else:
            if compare_trees(strip_tran, current_tree_tran, tree_tran, "east"):
                print("east transpose visible")
                visible += 1

        score1 = compare_trees(
            strip_norm, current_tree_norm, tree_norm, "west", 1)
        score2 = compare_trees(
            strip_norm, current_tree_norm, tree_norm, "east", 1)
        score3 = compare_trees(
            strip_tran, current_tree_tran, tree_tran, "west", 1)
        score4 = compare_trees(
            strip_tran, current_tree_tran, tree_tran, "east", 1)

        scenic_score.append(score1*score2*score3*score4)

print("overall visible", visible)
print("max scenic score", max(scenic_score))
