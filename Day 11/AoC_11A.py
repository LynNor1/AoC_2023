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
new_map = list()
for irow in range(num_rows):
    new_row = list()
    for icol in range(num_cols):
        new_row.append(map[irow][icol])
        if icol in empty_col_list:
            new_row.append(empty_char)
    new_map.append(new_row)
    if not galaxy_char in new_row:
        new_map.append(new_row)

print ("Expanded map:")
for row in new_map:
    print(convert(row))

# 3) find all the galaxies and their row, cols
num_cols = len(new_map[0])
num_rows = len(new_map)
galaxy_list = list()
for irow in range(num_rows):
    for icol in range(num_cols):
        if new_map[irow][icol] == galaxy_char:
            galaxy_list.append((irow, icol))
num_galaxies = len(galaxy_list)

# now find shortest distances between all galaxies
sum_distance = 0
for igal in range(num_galaxies-1):
    for igal2 in range(igal+1,num_galaxies):
        dist = abs(galaxy_list[igal2][0] - galaxy_list[igal][0]) + abs(galaxy_list[igal2][1] - galaxy_list[igal][1])
        sum_distance += dist

print (sum_distance)
