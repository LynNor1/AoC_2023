import re
import os

filename = "day1A_inputdata.txt"
# filename = "day1A_testDAta.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()
 
sum = 0
# Strips the newline character
for line in Lines:
    # get first digit
    first_match = re.search(r'^\D*(\d)', line)
    last_match = re.search(r'(\d)\D*$', line)
    first_digit = ""
    if first_match:
        first_digit = first_match.group(1)
        # print ("first digit: " + first_digit)
    last_digit = ""
    if last_match:
        last_digit = last_match.group(1)
        # print ("last digit: " + last_digit)
    combined_str = first_digit+last_digit
    # print ("combined string: " + combined_str)
    num = int(combined_str)
    # print (f"  converted to int: {num}")
    sum += num

print (sum)
