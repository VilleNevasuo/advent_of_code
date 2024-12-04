

def p1():

    total = 0
    with open("input.txt") as file:
        for line in file:
            sum = 0
            winnings = []
            line = line.strip().split(":")
            line  = line[1].strip().split("|")
            my_cards = line[1].strip().split(" ")
            winning_cards = line[0].strip().split(" ")
            winning_cards = [x for x in winning_cards if len(x) > 0]
            my_cards = [x for x in my_cards if len(x) > 0]
            
            for el in my_cards:
                if el in winning_cards:
                    winnings.append(el)
            for i in range(len(winnings)):
                if len(winnings) == 1:
                    sum += 1
                    break
                if len(winnings) > 0 and i == 1:
                    sum = sum + 1
                sum = sum * 2
                
            total += sum
            
    return total


def p2():
    
    total_scratchcards = []
    scratchcards = []

    with open("input.txt") as file:
        for index, line in enumerate(file):
            

            line = line.strip().split(":")
            line  = line[1].strip().split("|")
            my_numbers = line[1].strip().split(" ")
            winning_numbers = line[0].strip().split(" ")
            winning_numbers = [x for x in winning_numbers if len(x) > 0]
            my_numbers = [x for x in my_numbers if len(x) > 0]

            cards = {"id": index + 1, "winning_numbers": winning_numbers,"my_numbers": my_numbers}

            
            scratchcards.append(cards)
        
        
        cards_to_process = list(scratchcards)
        
        while cards_to_process:
            new_scratchcards = []

            for card_dict in cards_to_process:
                matches = 0
                for num in card_dict["winning_numbers"]:
                    if num in card_dict["my_numbers"]:
                        matches += 1
                
                
                current_card_id = card_dict["id"]
                for i in range(1, matches+1):
                    next_card_id = current_card_id + i
                    if next_card_id < len(scratchcards):
                            next_card = scratchcards[next_card_id -1]
                            new_scratchcards.append(next_card)
            
            
            total_scratchcards.extend(cards_to_process)
            cards_to_process = new_scratchcards
            
            
            
    return len(total_scratchcards)


#print(p1())
print(p2())