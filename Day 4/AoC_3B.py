import os

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

cards = list()
winning_nums_list = list()
card_nums_list = list()
num_wins = list()

for line in Lines:

    clean_line = line.strip()

    # get the card #
    card_tokens = clean_line.split(':')
    tokens = card_tokens[0].split()
    card_num = int(tokens[1].strip())
    cards.append(card_num)

    # get the two sets of numbers
    number_sets = card_tokens[1].split('|')

    # get the winning numbers
    winning_nums = number_sets[0].split()
    win_list = list()
    for winning_num in winning_nums:
        num = int(winning_num.strip())
        win_list.append(num)
    winning_nums_list.append(win_list)

    # get the card numbers
    card_nums = number_sets[1].split()
    num_list = list()
    for card_num in card_nums:
        num = int(card_num.strip())
        num_list.append(num)
    card_nums_list.append(num_list)

    # calculate the score
    num_matches = 0
    for win in win_list:
        if win in num_list:
            num_matches += 1
    num_wins.append(num_matches)

for i in range(len(cards)):
    print (f"card {i}: {num_wins[i]} wins")

# post-process cards and wins
new_card_indices = list()
for i in range(len(cards)):
    new_card_indices.append(i)
idx = 0

while idx < len(new_card_indices):
    og_card_idx = new_card_indices[idx]
    wins = num_wins[new_card_indices[idx]]
    if wins > 0:
        for win in range(wins):
            if og_card_idx+win+1 < len(cards):
                new_card_indices.append(og_card_idx+win+1)

    # print list so far (with wins)
    # print (f"idx {idx}:")
    # for i in range(len(new_card_indices)):
    #     new_card_index = new_card_indices[i]
    #     star = ""
    #     if i == idx:
    #         star = "*"
    #     print (f"{star}{i}: {cards[new_card_index]} wins {num_wins[new_card_index]}")

    idx += 1
    if idx%1000 == 0:
        print (f"# cards at {idx}: {len(new_card_indices)}")

print(len(new_card_indices))