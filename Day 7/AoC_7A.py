import os
import math

filename = "input_data.txt"

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
# hand_types.sort()

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
print ("Unsorted cards:")
for hand_type in hand_types:
    og_idx = hand_type[1]
    print (f"{og_idx}) {cards[og_idx]} bet {bets[og_idx]} score {hand_type[0]}")

# now sort the ties by highest card from left
sorted_hand_types = list()
total_count = 0
for ht in range(0,7):

    # grab all the cards with this score or hand type
    new_list = list()
    for hand_type in hand_types:
        if hand_type[0] == ht:
            new_list.append(hand_type)

    # now we need to sort create a list of all the
    # converted cards and their original indices
    new_list_to_sort = list()
    for item in new_list:
        og_idx = item[1]
        new_list_to_sort.append([sub_cards[og_idx], og_idx])

    # now sort the new_list_to_sort alphabetically
    new_list_to_sort.sort()

    # now build the sorted_handtypes
    for idx in range(len(new_list_to_sort)):
        total_count += 1
        og_idx = new_list_to_sort[idx][1]
        sorted_hand_types.append (hand_types[og_idx])

print (f"Total count {total_count}")

#print final card list
print ("Sorted cards:")
for hand_type in sorted_hand_types:
    og_idx = hand_type[1]
    print (f"{og_idx}) {cards[og_idx]} ({sub_cards[og_idx]}) bet {bets[og_idx]} score {hand_type[0]}")

# compute score
score = 0
N = len(sorted_hand_types)
for idx in range(N):
    og_idx = sorted_hand_types[idx][1]
    # print (f"Scoring {bets[og_idx]} * {N-idx}")
    score += (N-idx)*bets[og_idx]

print(len(hand_types))
print(len(sorted_hand_types))

print(score)