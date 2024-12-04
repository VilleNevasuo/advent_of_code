from collections import Counter




def is_full_house(s):
    counter = Counter(s)
    return set(counter.values()) == {2, 3}

def is_four_of_a_kind(s):
    counter = Counter(s)
    return 4 in counter.values()

def is_three_of_a_kind(s):
    counter = Counter(s)
    return 3 in counter.values() and len(counter) == 3

def is_two_pair(s):
    counter = Counter(s)
    return list(counter.values()).count(2) == 2

def is_one_pair(s):
    counter = Counter(s)
    return list(counter.values()).count(2) == 1


def replace_jokers(hand):

    card_count = Counter(card for card in hand if card != 'J')

    if card_count:
        most_common_card = card_count.most_common(1)[0][0]

        hand = hand.replace("J", most_common_card)

    return hand


def sort_cards(cards):
    ranking = "AKQT98765432J"

    def sort_key(card):
        power = card[-1]
        hand = card[0]

        hand_ranks = tuple(ranking.index(h) for h in hand)

        return (-power, hand_ranks)

    return sorted(cards, key=sort_key)


def calculate_ranks(hands_bids):

    cards = []
    for pair in hands_bids:
        card = []
        hand = pair[0]
        bid = pair[1]

        card.append(hand)
        card.append(bid)


        hand = replace_jokers(hand)

        if hand == len(hand) * hand[0]:
            card.append(7)
        elif is_four_of_a_kind(hand):
            card.append(6)
        elif is_full_house(hand):
            card.append(5)
        elif is_three_of_a_kind(hand):
            card.append(4)
        elif is_two_pair(hand):
            card.append(3)
        elif is_one_pair(hand):
            card.append(2)
        else:
            card.append(1)

        cards.append(card)
    

    return cards
    


def p2():

    total = 0
    hands_bids = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split()
            pair = (line[0], line[1])
            hands_bids.append(pair)
    
    cards = calculate_ranks(hands_bids)
    

    cards = sort_cards(cards)
    print(cards)
    
    for index, card in enumerate(reversed(cards)):
        
        
        bid = card[1]
        subtotal = (index+1) * int(bid)
        total = total + subtotal
    

    return total


print(p2())
