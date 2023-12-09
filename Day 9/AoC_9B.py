import os
import math

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

sum_last_vals = 0

for line in Lines:
    # read all the numbers
    tokens = line.strip().split()
    # convert to ints
    int_list = [int(token) for token in tokens]

    diff_lists = list()
    diff_lists.append(int_list)

    all_zeros = False
    start_list = int_list
    # calculate diffs until they're all 0s
    while not all_zeros:
        diff_list = list()
        for idx in range (len(start_list)-1):
            diff_list.append(start_list[idx+1]-start_list[idx])
        diff_lists.append(diff_list)
        not_zero_list = [d for d in diff_list if d != 0]
        all_zeros = len(not_zero_list) == 0
        start_list = diff_list
    
    # calculate prior value
    new_val = 0
    for i in reversed(range (len(diff_lists)-1)):
        new_val = diff_lists[i][0] - new_val

    sum_last_vals += new_val    

print(sum_last_vals)