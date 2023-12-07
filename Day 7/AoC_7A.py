import os
import math

filename = "test_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

card_list = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
sub_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
cards = list()
bets = list()

for line in Lines:
    clean_line = line.strip()
    tokens = clean_line.split()

    cards.append(tokens[0].strip())
    bets.append(int(tokens[1].strip()))

# hierarchy of hands:
# 0) five-of-a-kind
# 1) four-of-a-kind
# 2) full house
# 3) three of a kind
# 4) two pairs
# 5) one pair
# 6) high card

hand_types = [0 for x in range(len(cards))]

# Establish type of hand for each hand
for idx in range(len(cards)):
    count_list = [0 for x in range(13)]
    # count # of cards in each hand
    for char in cards[idx]:
        # get index of this char in the char_list
        i = card_list.index(char)
        count_list[i] += 1
    # check for all of the different hand types
    if 5 in count_list:
        hand_types[idx] = (0, idx)
    elif 4 in count_list:
        hand_types[idx] = (1, idx)
    elif 3 in count_list and 2 in count_list:
        hand_types[idx] = (2, idx)
    elif 3 in count_list:
        hand_types[idx] = (3, idx)
    elif count_list.count(2) == 2:
        hand_types[idx] = (4, idx)
    elif 2 in count_list:
        hand_types[idx] = (5, idx)
    else:
        hand_types[idx] = (6, idx)

# now sort hands by hand_type
hand_types.sort()

def convert_to_alpha (myhand):
    newhand = ""
    for char in myhand:
        idx = card_list.index(char)
        newhand += sub_list[idx]
    return newhand

# convert all hands to hands I can alphabetize
sub_cards = list()
for card in cards:
    sub_cards.append(convert_to_alpha(card))

# print final card list
# print ("Unsorted cards:")
# for hand_type in hand_types:
#     og_idx = hand_type[1]
#     print (f"{og_idx}) {cards[og_idx]} bet {bets[og_idx]} score {hand_type[0]}")

# now sort the ties by highest card from left
for ht in range(6):
    count = 0
    match_idx = list()
    for idx in range (len(hand_types)):
        if hand_types[idx][0] == ht:
            count += 1
            match_idx.append(idx)
    if count > 1:
        list_to_sort = list()
        for match in match_idx:
            list_to_sort.append((sub_cards[match], match))
        list_to_sort.sort()
        # make a copy of the hand_types
        new_hand_types = list()
        for hand_type in hand_types:
            new_hand_types.append(hand_type)
        # now update the sorted hand_types
        for idx in range(count):
            m_idx = match_idx[idx]
            new_hand_types[m_idx] = hand_types[list_to_sort[idx][1]]
        hand_types = new_hand_types

#print final card list
print ("Sorted cards:")
for hand_type in hand_types:
    og_idx = hand_type[1]
    print (f"{og_idx}) {cards[og_idx]} ({sub_cards[og_idx]}) bet {bets[og_idx]} score {hand_type[0]}")

# compute score
score = 0
N = len(hand_types)
for idx in range(N):
    og_idx = hand_types[idx][1]
    # print (f"Scoring {bets[og_idx]} * {N-idx}")
    score += (N-idx)*bets[og_idx]

print(score)