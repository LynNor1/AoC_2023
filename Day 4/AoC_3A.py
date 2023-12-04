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

sum = 0
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
    score = 0
    for win in win_list:
        if win in num_list:
            if score == 0:
                score = 1
            else:
                score *= 2

    sum += score

print (sum)