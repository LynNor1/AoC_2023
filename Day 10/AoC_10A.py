import os
import math

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

# read in map and find the S at the same
# time
map = list()
start_row = -1
start_col = -1
cnt = 0
for line in Lines:
    map.append(line.strip())
    find_s = line.strip().find('S')
    if find_s >= 0:
        start_row = cnt
        start_col = find_s
    cnt += 1

num_rows = cnt
num_cols = len(map[0])

def can_go_left():
    return cur_col > 0 and map[cur_row][cur_col-1] != '.'

def can_go_right():
    return cur_col < num_cols-1 and map[cur_row][cur_col+1] != '.'

def can_go_up():
    return cur_row > 0 and map[cur_row-1][cur_col] != '.'

def can_go_down():
    return cur_row < num_rows-1 and map[cur_row+1][cur_col] != '.'

cur_row = start_row
cur_col = start_col

# find the one cell around starting
# position that I can actually connect to
found_next = False
if can_go_up() and (map[cur_row-1][cur_col]=='|' or map[cur_row-1][cur_col]=='F' or map[cur_row-1][cur_col]=='7'):
    next_row = cur_row-1
    next_col = cur_col
    next_char = map[next_row][next_col]
    found_next = True
if not found_next and can_go_down() and (map[cur_row+1][cur_col]=='|' or map[cur_row+1][cur_col]=='L' or map[cur_row+1][cur_col]=='J'):
    next_row = cur_row+1
    next_col = cur_col
    next_char = map[next_row][next_col]    
    found_next = True
if not found_next and can_go_right() and (map[cur_row][cur_col+1]=='-' or map[cur_row][cur_col+1]=='J' or map[cur_row][cur_col+1]=='7'): 
    next_row = cur_row
    next_col = cur_col+1
    next_char = map[next_row][next_col]    
    found_next = True
if not found_next and can_go_left() and (map[cur_row][cur_col+1]=='-' or map[cur_row][cur_col+1]=='F' or map[cur_row][cur_col+1]=='L'):
    next_row = cur_row
    next_col = cur_col+1
    next_char = map[next_row][next_col]    
    found_next = True

if not found_next:
    print ("SOMETHING IS WRONG!")

def go_up():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char    
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_row -= 1
    next_char = map[next_row][next_col]
def go_down():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_row += 1
    next_char = map[next_row][next_col]
def go_right():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_col += 1
    next_char = map[next_row][next_col]
def go_left():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char
    next_col -= 1
    next_char = map[next_row][next_col]            

# follow loop and count # of steps
finished = False
steps = 0
cur_char = map[cur_row][cur_col]
while not finished:
    # print (f"{cur_row} {cur_col} {cur_char} => {next_row} {next_col} {next_char}")
    if next_char == '-':
        if next_col > cur_col:
            go_right()
        elif next_col < cur_col:
            go_left()
        else:
            print ("SOMTHING WRONG -")
    elif next_char == '|':
        if next_row < cur_row:
            go_up()
        elif next_row > cur_row:
            go_down()
        else:
            print ("SOMETHING WRONG |")
    elif next_char == '7':
        if next_row < cur_row:
            go_left()
        elif next_col > cur_col:
            go_down()
        else:
            print ("SOMETHING WRONG 7")
    elif next_char == 'J':
        if next_row > cur_row:
            go_left()
        elif next_col > cur_col:
            go_up()
        else:
            print ("SOMETHING WRONG J")
    elif next_char == 'L':
        if next_row > cur_row:
            go_right()
        elif next_col < cur_col:
            go_up()
        else:
            print ("SOMETHING WRONG L")
    elif next_char == 'F':
        if next_row < cur_row:
            go_right()
        elif next_col < cur_col:
            go_down()
        else:
            print ("SOMETHING WRONG F")
    steps += 1
    if next_char == 'S':
        finished = True

print (math.floor(steps/2)+1)
    