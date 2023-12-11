import os
import math

filename = "input_data.txt"

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

map = list()

for line in Lines:
    map.append([x for x in line.strip()])

num_cols = len(map[0])
num_rows = len(map)

galaxy_char = '#'
empty_char = '.'

# now expand the universe
# 1) get list of columns containing no #s
empty_col_list = list()
for icol in range(num_cols):
    no_galaxies = True
    for irow in range(num_rows):
        if map[irow][icol] == galaxy_char:
            no_galaxies = False
    if no_galaxies:
        empty_col_list.append(icol)

# 2) expand our columns and rows at the same time
multiplier = 1000000
galaxy_int = 0
new_map = list()
for irow in range(num_rows):
    new_row = list()
    for icol in range(num_cols):
        sub_int = galaxy_int # galaxy
        if map[irow][icol] == '.':
            sub_int = 1 # empty space (1 step)
        if icol in empty_col_list:
            sub_int = multiplier # expanded space (1000000 steps)
        new_row.append(sub_int)
    if not galaxy_int in new_row:
        new_map.append([multiplier for i in range(num_cols)])
    else:
        new_map.append(new_row)

print ("Expanded map:")
for row in new_map:
    print(row)

# 3) find all the galaxies and their row, cols
#    and reset their vals to 1 so it doesn't mess
#    our distance calculations
galaxy_list = list()
for irow in range(num_rows):
    for icol in range(num_cols):
        if new_map[irow][icol] == galaxy_int:
            galaxy_list.append((irow, icol))
            # new_map[irow][icol] == 1
num_galaxies = len(galaxy_list)

# now find shortest distances between all galaxies
sum_distance = 0
for igal in range(num_galaxies-1):
    for igal2 in range(igal+1,num_galaxies):
        irow_start = galaxy_list[igal2][0]
        irow_end = galaxy_list[igal][0]
        icol_start = galaxy_list[igal2][1]
        icol_end = galaxy_list[igal][1]
        irow_dir = 1 if irow_end > irow_start else -1
        icol_dir = 1 if icol_end > icol_start else -1
        dist = 0
        count_zeros = 0
        for icol in range(icol_start, icol_end+icol_dir, icol_dir):
            irow = irow_start
            # print (f"at {irow} {icol} value {new_map[irow][icol]}")
            dist += new_map[irow][icol]
            if new_map[irow][icol] == 0:
                count_zeros += 1        
        for irow in range(irow_start+irow_dir, irow_end+irow_dir, irow_dir):
            icol = icol_end
            # print (f"at {irow} {icol} value {new_map[irow][icol]}")
            dist += new_map[irow][icol]
            if new_map[irow][icol] == 0:
                count_zeros += 1            
        dist += (count_zeros - 1)
        # print (f"dist between {irow_start} {icol_start} to {irow_end} {icol_end}: {dist}")
        
        sum_distance += dist

print (sum_distance)
