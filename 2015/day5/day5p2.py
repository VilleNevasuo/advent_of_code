

def process_3_chunk(word):

    for i in range(0, len(word)):
        if i + 3 < len(word) +1:
            
            block = word[i:i+3]
            if block[0] == block[2]:
                return True
            
    return False


def process_2_pairs(word):

    #iterate over the original word
    for i in range(len(word)):

        #capture the pair 
        if i+1 < len(word):
            pair = word[i:i+2]

            #create a modified word by removing the pair from it for comparison.

            mod_word = word[:i]
            mod_word2 = word[i+2:]

            #iterate over the modified word
            for j in range(len(mod_word)):

                #capture a pair from the modified word
                if j+1 < len(mod_word):
                    pair2 = mod_word[j:j+2]

                    #if identifical pair exists, word is nice
                    if pair == pair2:
                        return True 

            #same as above but for the other word
            if i > 1:
                for k in range(len(mod_word2)):
                    if j+1 < len(mod_word2):
                        pair3 = mod_word2[k:k+2]
                        if pair == pair3:
                            return True

    return False


def process_word():

    nice = 0

    with open("input.txt") as file:
        for word in file:
            
            word = word.strip()
            block_3_nice = process_3_chunk(word)
            pairs_nice = process_2_pairs(word)


            if block_3_nice and pairs_nice:
                
                print(word)
                nice += 1
    
    print(nice)
    


process_word()

