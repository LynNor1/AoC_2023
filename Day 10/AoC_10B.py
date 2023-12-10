import os
import math

filename = "input_data.txt"

def convert(s): 
    new = "" 
    for x in s: 
        new += x 
    return new 

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

save_next_row = next_row
save_next_col = next_col
save_next_char = next_char

do_print = False

def go_up():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char    
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_row -= 1
    next_char = map[next_row][next_col]
    if do_print:
        print ("  up")
def go_down():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_row += 1
    next_char = map[next_row][next_col]
    if do_print:
        print ("  down")    
def go_right():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char    
    next_col += 1
    next_char = map[next_row][next_col]
    if do_print:
        print ("  right")    
def go_left():
    global cur_row, cur_col, cur_char, next_row, next_col, next_char        
    cur_row = next_row
    cur_col = next_col
    cur_char = next_char
    next_col -= 1
    next_char = map[next_row][next_col]           
    if do_print:
        print ("  left")

empty_char = " "
inside_char = 'o'
clean_map = [ [empty_char]*num_cols for i in range(num_rows)]

# follow loop and make a map of just the loop
finished = False
steps = 0
cur_char = map[cur_row][cur_col]
clean_map[cur_row][cur_col] = 'S'
while not finished:
    clean_map[next_row][next_col] = next_char
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

print ("Clean map with loop:")
for row in range(num_rows):
    print (convert(clean_map[row]))

def mark_is_empty(row_incr, col_incr):
    global clean_map
    check_row = cur_row+row_incr
    check_col = cur_col+col_incr
    if check_row >= 0 and check_row < num_rows and check_col >= 0 and check_row < num_cols and clean_map[check_row][check_col] == empty_char:
        clean_map[check_row][check_col] = inside_char
        if do_print:
            for row in range(num_rows):
                print (convert(clean_map[row]))            

finished = False
# do_print = True
cur_row = start_row
cur_col = start_col
cur_char = map[cur_row][cur_col]
next_row = save_next_row
next_col = save_next_col
next_char = save_next_char
while not finished:
    if do_print:
        print (f"{cur_row} {cur_col} {cur_char} => {next_row} {next_col} {next_char}")
    # '*' in the notation is previous position
    # 'x' shows where we need to check if empty after the move
    # looking-to-the-left
    if next_char == '-':
        if next_col > cur_col:
            #   x
            # * -
            go_right()            
            mark_is_empty(-1,0) 
        elif next_col < cur_col:
            # - *
            # x
            go_left()                
            mark_is_empty(1,0)     
        else:
            print ("SOMTHING WRONG -")
    elif next_char == '|':
        if next_row < cur_row:
            # x |
            #   *
            go_up()           
            mark_is_empty(0,-1)             
        elif next_row > cur_row:
            #  *
            #  | x
            go_down()            
            mark_is_empty(0,1)            
        else:
            print ("SOMETHING WRONG |")
    elif next_char == '7':
        if next_row < cur_row:
            #   7
            # x *
            go_left()      
            mark_is_empty(1,-1)           
        elif next_col > cur_col:
            #   x x
            # * 7 x
            go_down()           
            mark_is_empty(0,1)    
            mark_is_empty(-1,1)
            mark_is_empty(-1,0)         
        else:
            print ("SOMETHING WRONG 7")
    elif next_char == 'J':
        if next_row > cur_row:
            #   *
            #   J x
            #   x x
            go_left()   
            mark_is_empty(0,1)    
            mark_is_empty(1,1)
            mark_is_empty(1,0)                  
        elif next_col > cur_col:
            # x
            # * J
            go_up()            
            mark_is_empty(-1,-1)                                   
        else:
            print ("SOMETHING WRONG J")
    elif next_char == 'L':
        if next_row > cur_row:
            #   * x
            #   L
            go_right()          
            mark_is_empty(-1,1)                                                  
        elif next_col < cur_col:
            # x L *
            # x x
            go_up()              
            mark_is_empty(0,-1)   
            mark_is_empty(1,-1)   
            mark_is_empty(1,0)                                   
        else:
            print ("SOMETHING WRONG L")
    elif next_char == 'F':
        if next_row < cur_row:
            # x x
            # x F
            #   *
            go_right()            
            mark_is_empty(0,-1)         
            mark_is_empty(-1,-1)
            mark_is_empty(-1,0)   
        elif next_col < cur_col:
            # F *
            #   x
            go_down()                      
            mark_is_empty(1,1)     
        else:
            print ("SOMETHING WRONG F")
    steps += 1
    if next_char == 'S':
        finished = True

print ("First pass marking empty spaces-to-left:")
for row in range(num_rows):
    print (convert(clean_map[row]))        

# expand all o's to adjacent empty spots
something_changed = True
iter = 0
while something_changed:
    something_changed = False
    for row in range(num_rows):
        for col in range(num_cols):
            if clean_map[row][col] == inside_char:
                if (col < num_cols-1) and clean_map[row][col+1] == empty_char:
                    clean_map[row][col+1] = inside_char
                    something_changed = True
                if (row < num_rows-1) and clean_map[row+1][col] == empty_char:
                    clean_map[row+1][col] = inside_char
                    something_changed = True                    
                if (col > 0) and clean_map[row][col-1] == empty_char:
                    clean_map[row][col-1] = inside_char
                    something_changed = True                    
                if (row > 0) and clean_map[row-1][col] == empty_char:
                    clean_map[row-1][col] = inside_char
                    something_changed = True      
    iter += 1
    # print (f"Iteration {iter}:")
    # for row in range(num_rows):
    #     print (convert(clean_map[row]))     

print ("Expanded clean map:")
for row in range(num_rows):
    print (convert(clean_map[row]))        

# if any o's are on the outside boundaries,
# then we know that the inside "tiles" are
# all still empty

def o_on_edge():
    first_line = convert(clean_map[0])
    last_line = convert(clean_map[-1])
    first_col_list = [i[0] for i in clean_map]
    last_col_list = [i[-1] for i in clean_map]
    first_col = convert(first_col_list)
    last_col = convert(last_col_list)    
    if first_line.find(inside_char) >= 0:
        return True
    if last_line.find(inside_char) >= 0:
        return True
    if first_col.find(inside_char) >= 0:
        return True
    if last_col.find(inside_char) >= 0:
        return True
    return False

def count_map(which_char):
    cnt = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if clean_map[r][c] == which_char:
                cnt += 1
    return cnt

if o_on_edge():
    print (count_map(empty_char))
else:
    print (count_map(inside_char))
        