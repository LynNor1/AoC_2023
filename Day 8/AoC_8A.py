import os
import math

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

instructions = ""
maps = {}

for line in Lines:
    clean_line = line.strip()
    tokens = clean_line.split('=')

    if len(tokens) == 2:
        key = tokens[0].strip()
        clean_str = tokens[1].strip().replace('(','').replace(')','')
        map_tokens = clean_str.split(',')
        token_list = list()
        for map_token in map_tokens:
            token_list.append(map_token.strip())
        maps[key] = token_list

    elif len(tokens) == 1 and len(tokens[0].strip()) > 0:
        instructions = tokens[0].strip()

# print (f"{instructions}")
# for map in maps:
#     print (f"{map} {maps[map]}")

# follow instructions
start_goal = 'AAA'
end_goal = 'ZZZ'
next_step_idx = 0
num_steps = len(instructions)
at_goal = start_goal

count_steps = 0
while at_goal != end_goal:
    # get next step (R or L)
    step = instructions[next_step_idx]
    next_step_idx += 1
    if next_step_idx == num_steps:
        next_step_idx = 0
    # get map for current location
    map = maps[at_goal]
    # get next location
    if step == 'R':
        at_goal = map[1]
    else:
        at_goal = map[0]
    count_steps += 1

print(count_steps)