import os
import math

filename = "test_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

def convert(s): 
    new = "" 
    for x in s: 
        new += x 
    return new 

puzzles = list()
clues = list()

puzzles2 = list()

for line in Lines:
    tokens = line.strip().split()
    puzzles.append(tokens[0].replace('.',' '))
    puzzles2.append(tokens[0].replace('.', ' ') + "?")
    clue_tokens = tokens[1].split(',')
    clue_list = list()
    for clue in clue_tokens:
        clue_list.append(int(clue))
    clues.append(clue_list)

def check_puzzle_against_clues (puzz, clues):
    # puzz is a string with no '?'s and all '.'s converted to ' 's
    # clues is the list of clues for the line
    tokens = puzz.split()
    if len(clues) != len(tokens):
        return False
    else:
        for i in range(len(clues)):
            if clues[i] != len(tokens[i]):
                return False
        return True
    
# recursive routine to try each possible value of ? (either '#' or ' ')
# and return 1 if the answer will work with the clues or 0 if not
def process_next_unknown (puzz, clues, count: int):
    next_unknown_idx = puzz.find('?')
    if next_unknown_idx >= 0:
        new_puzz_empty = puzz.replace('?', ' ', 1)
        new_puzz_filled = puzz.replace("?", '#', 1)
        count = process_next_unknown (new_puzz_empty, clues, count)
        count = process_next_unknown (new_puzz_filled, clues, count)
        return count
    else:
        if check_puzzle_against_clues (puzz, clues):
            return count+1
        else:
            return count

sum_count = 0
save_counts = list()
save_counts2 = list()
times_five_sum = 0
for i in range(len(puzzles)):
    final_count = process_next_unknown (puzzles[i], clues[i], 0)
    save_counts.append(final_count)
    sum_count += final_count
    final_count2 = process_next_unknown (puzzles2[i], clues[i], 0)
    save_counts2.append(final_count2)
    times_five_count = final_count2*final_count2*final_count2*final_count2*final_count
    times_five_sum += times_five_count

print (sum_count)

print (times_five_sum)