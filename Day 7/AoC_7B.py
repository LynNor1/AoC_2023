import os
import math

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

card_list = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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
hand_msgs = ["5-of-a-kind", "4-of-a-kind", "full house", "3 of a kind", "2 pairs", "1 pair", "high card"]

# Establish type of hand for each hand
for idx in range(len(cards)):
    count_list = [0 for x in range(13)]
    # count # of cards in each hand
    for char in cards[idx]:
        # get index of this char in the char_list
        i = card_list.index(char)
        count_list[i] += 1
    num_jokers = count_list[12]
    num_5count = count_list.count(5)
    # the following need to exclude jokers as part of their count
    num_4count = count_list[0:12].count(4) 
    num_3count = count_list[0:12].count(3)
    num_2count = count_list[0:12].count(2)
    num_1count = count_list[0:12].count(1)
    # check for all of the different hand types
    if num_5count==1 or (num_4count==1 and num_jokers==1) or (num_3count==1 and num_jokers==2) or (num_2count==1 and num_jokers==3) or (num_1count==1 and num_jokers==4):
        hand_types[idx] = (0, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as 5-of-a-kind")
    elif num_4count==1 or (num_3count==1 and num_jokers==1) or (num_2count==1 and num_jokers==2) or (num_1count==1 and num_jokers==3):
        hand_types[idx] = (1, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as 4-of-a-kind")        
    elif (num_3count==1 and num_2count==1) or (num_2count==2 and num_jokers==1) or (num_3count==1 and num_jokers==1) or (num_2count==1 and num_jokers==2):
        hand_types[idx] = (2, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as full house")            
    elif num_3count==1 or (num_2count==1 and num_jokers==1) or num_jokers == 2:
        hand_types[idx] = (3, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as 3-of-a-kind")                
    elif num_2count==2:
        hand_types[idx] = (4, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as 2 pairs")            
    elif num_2count==1 or num_jokers==1:
        hand_types[idx] = (5, idx)
        if (num_jokers > 0):
            print (f"  {idx}) {cards[idx]} scored as 1 pair")              
    elif num_jokers == 3:
        hand_types[idx] = (1, idx)
        print (f"  {idx}) {cards[idx]} scored as 4-of-a-kind")   
    else:
        hand_types[idx] = (6, idx)
        if (num_jokers > 0):
            print ("SOMETHING IS WRONG!")

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
    extra_msg = ""
    if cards[og_idx].count('J') > 0:
        extra_msg = "*"    
    print (f"{og_idx}) {cards[og_idx]} bet {bets[og_idx]} {hand_msgs[hand_type[0]]} {extra_msg}")

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
    extra_msg = ""
    if cards[og_idx].count('J') > 0:
        extra_msg = "*"
    print (f"{og_idx}) {cards[og_idx]} ({sub_cards[og_idx]}) bet {bets[og_idx]} {hand_msgs[hand_type[0]]} {extra_msg}")

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