

nice = 0
vowellist = "aeiou"

with open("input.txt") as file:
    for word in file:
        vowels = 0
        twice_in_a_row = False
        does_not_contain_bad_stuff = False
        for i,char in enumerate(word):
            if char in vowellist:
                vowels += 1
            if i > 0:
                if word[i-1] == char:
                    twice_in_a_row = True
        if "ab" not in word and "cd" not in word and "pq" not in word and "xy" not in word:
            does_not_contain_bad_stuff = True
        
        if vowels >= 3 and twice_in_a_row and does_not_contain_bad_stuff:
            nice += 1
    
    print(nice)






#pseudo

#iterate over rows
# if obstacles
#check vowels with 