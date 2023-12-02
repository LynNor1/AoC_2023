import re

filename = "day1A_inputdata.txt"
# filename = "day1A_testData.txt"
# filename = "day1B_testData.txt"

# list of digits to search for
digit_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Using readlines()
file1 = open(filename, 'r')
Lines = file1.readlines()
 
sum = 0
# Strips the newline character
for line in Lines:

    # print("Testing:")
    # print (line)

    first_digit = ""
    first_digit_pos = 10000
    last_digit = ""
    last_digit_pos = -1    

    # get first digit
    first_match = re.search(r'^\D*(\d)', line)
    last_match = re.search(r'(\d)\D*$', line)

    if first_match:
        first_digit = first_match.group(1)
        first_digit_pos = first_match.start(1)
        # print (f"first digit: {first_digit} at position {first_digit_pos}" )
    if last_match:
        last_digit = last_match.group(1)
        last_digit_pos = last_match.start(1)
        # print (f"last digit: {last_digit} at position {last_digit_pos}")

    ll_line = str.lower(line)
    idx = 0
    for digit in digit_list:

        first_match_idx = ll_line.find(digit)
        if first_match_idx >= 0 and first_match_idx < first_digit_pos:
            first_digit = str(idx)
            first_digit_pos = first_match_idx
            # print (f"first digit: {digit} {first_digit} at position {first_digit_pos}" )                           

        # regex = f"^.*({digit})"
        # first_match = re.search (regex, ll_line)
        # if first_match:
        #     first_match_pos = first_match.start(1)
        #     if first_match_pos < first_digit_pos:
        #         first_digit = str(idx)
        #         first_digit_pos = first_match_pos
        #         # print (f"first digit: {digit} {first_digit} at position {first_digit_pos}" )                

        last_match_idx = ll_line.rfind(digit)
        if last_match_idx >= 0 and last_match_idx > last_digit_pos:
            last_digit = str(idx)
            last_digit_pos = last_match_idx
            # print (f"last digit: {digit} {last_digit} at position {last_digit_pos}")                

        # regex = f"({digit}.*$)"
        # last_match = re.search (regex, ll_line)
        # if last_match:
        #     last_match_pos = last_match.start(1)
        #     if last_match_pos > last_digit_pos:
        #         last_digit = str(idx)
        #         last_digit_pos = last_match_pos
        #         print (f"last digit: {digit} {last_digit} at position {last_digit_pos}")                
        idx += 1
    
    combined_str = first_digit+last_digit
    # print ("combined string: " + combined_str)
    print (f"{line} {combined_str}")
    num = int(combined_str)
    # print (f"  converted to int: {num}")
    sum += num

print (sum)
