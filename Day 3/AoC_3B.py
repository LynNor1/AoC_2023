import os

filename = "input_data.txt"

part_nums = list()
part_num_line = list()
part_num_start = list()
part_num_end = list()

symbols = list()
symbol_line = list()
symbol_loc = list()

accum_int_str = ""
str_start = 0
str_end = 0
line_num = 0

total_lines = 0

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

# first part is to get all of the numbers and
# their start/end locations in the grid
# 
# also we need the location of symbols in the
# grid
line_num = 0
for line in Lines:
    # print(line.strip())
    # process each line char-by-char to see if an int or
    # a symbol
    pos = 0
    for char in line.strip():
        # check if digit
        if char.isdigit():
            if not accum_int_str:
                str_start = pos
            str_end = pos
            accum_int_str += char
        elif char != '.':
            # process any accumulated int first
            if accum_int_str:
                part_nums.append(int(accum_int_str))
                part_num_line.append(line_num)
                part_num_start.append(str_start)
                part_num_end.append(str_end)
                accum_int_str = ""
            # process symbol
            symbols.append(char)
            symbol_line.append(line_num)
            symbol_loc.append(pos)
        else:
            # process any accumulated int
            if accum_int_str:
                part_nums.append(int(accum_int_str))
                part_num_line.append(line_num)
                part_num_start.append(str_start)
                part_num_end.append(str_end)
                accum_int_str = ""         

        pos += 1

    # process any accumulated int at end of line
    if accum_int_str:
        part_nums.append(int(accum_int_str))
        part_num_line.append(line_num)
        part_num_start.append(str_start)
        part_num_end.append(str_end)
        accum_int_str = ""   

    line_num += 1
    total_lines += 1

def sym_at_pos (line, start_pos, end_pos):
    if line < 0 or line >= total_lines:
        return False
    for sym_idx in range(len(symbol_line)):
        if symbol_line[sym_idx] == line and symbol_loc[sym_idx] >= start_pos and symbol_loc[sym_idx] <= end_pos:
            return True
        # stop processing if we've gone past the line of interest
        if symbol_line[sym_idx] > line:
            return False
    return False

def part_adj_to_pos (sym_line, sym_pos, part_idx):
    part_line = part_num_line[part_idx]
    part_start = part_num_start[part_idx]
    part_end = part_num_end[part_idx]
    if part_start > sym_pos+1 or part_end < sym_pos-1:
        return False
    # check if part_line within 1 of sym_line
    if abs(sym_line - part_line) <= 1:
        # any part of the string needs to be +/- 1 of sym_pos
        for str_pos in range (part_start, part_end+1):
            if str_pos >= sym_pos-1 and str_pos <= sym_pos+1:
                return True
    return False

# now let's find all the '*'s and count how many
# part numbers are adjacent to it

sum = 0
for sym_idx in range (len(symbols)):
    symbol = symbols[sym_idx]
    if symbol == '*':
        gear_list = list()
        for part_idx in range (len(part_nums)):
            if part_adj_to_pos (symbol_line[sym_idx], symbol_loc[sym_idx], part_idx):
                gear_list.append(part_nums[part_idx])
        if len(gear_list) == 2:
            sum += gear_list[0]*gear_list[1]
print (sum)

# # now let's find ints that are not adjacent to
# # symbols
# sum = 0
# for part_idx in range(len(part_nums)):
#     part_line = part_num_line[part_idx]
#     part_start = part_num_start[part_idx]
#     part_end = part_num_end[part_idx]
#     # look on same line first
#     adjacent = sym_at_pos (part_line, part_start-1, part_end+1)
#     # look on previous line
#     if not adjacent:
#         adjacent = sym_at_pos (part_line-1, part_start-1, part_end+1)
#     # look on next line
#     if not adjacent:
#         adjacent = sym_at_pos (part_line+1, part_start-1, part_end+1)

#     if adjacent:
#         sum += part_nums[part_idx]

#     # print (f"part num {part_nums[part_idx]} is adjacent: {adjacent}")

# print (sum)

