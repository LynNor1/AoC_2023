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
num_maps = 0

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
        num_maps += 1

    elif len(tokens) == 1 and len(tokens[0].strip()) > 0:
        instructions = tokens[0].strip()

# print (f"{instructions}")
# for map in maps:
#     print (f"{map} {maps[map]}")

print (f"Total # of maps: {num_maps}")

# find all the starting goals
starting_goals = list()
for map_key in maps:
    if map_key.endswith('A'):
        starting_goals.append(map_key)

# follow instructions
next_step_idx = 0
num_steps = len(instructions)
at_goals = starting_goals

def all_goals_end_with_z (goals):
    for goal in goals:
        if not goal.endswith('Z'):
            return False
    return True

# apparently each starting goal has it's
# own cycle that repeats over and over again
# so we need to find the # of steps for the cycle
# to get to a goal that ends with 'Z'
cycles = list()
z_steps = list()

for goal in starting_goals:

    print (f"Establishing cycle for {goal}")

    count_steps = 0
    next_step_idx = 0
    next_goal = goal

    finished_loop = False
    found_z = False
    encountered = list()
    encountered.append(goal)
    while not finished_loop:
       # get next step (R or L)
        step = instructions[next_step_idx]
        next_step_idx += 1
        if next_step_idx == num_steps:
            next_step_idx = 0

        map = maps[next_goal]
        # get next location
        if step == 'R':
            next_goal = map[1]
        else:
            next_goal = map[0]

        if count_steps%100 == 0:
            print (f"  at count {count_steps} {next_goal}")

        count_steps += 1

        if not found_z and next_goal.endswith("Z"):
            found_z = True
            z_steps.append(count_steps)
            z_offset = count_steps        

        if next_goal in encountered:
            finished_loop = True
            break

        encountered.append(next_goal)

    cycles.append(count_steps)

    print (f"cycles for goal {goal}: {count_steps} z offset: {z_offset}")

# count_steps = 0
# while not all_goals_end_with_z (at_goals):
#     # get next step (R or L)
#     step = instructions[next_step_idx]
#     next_step_idx += 1
#     if next_step_idx == num_steps:
#         next_step_idx = 0

#     # move to next location for all goals
#     new_goals = list()
#     for goal in at_goals:
#         # get map for current location
#         map = maps[goal]
#         # get next location
#         if step == 'R':
#             new_goals.append(map[1])
#         else:
#             new_goals.append(map[0])
#     at_goals = new_goals

#     if count_steps%100 == 0:
#         print (f"step {count_steps} {at_goals}")
#     count_steps += 1

print(count_steps)