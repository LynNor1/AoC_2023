import os
import math

filename = "final_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

times = list()
distances = list()

for line in Lines:
    clean_line = line.strip()
    tokens = clean_line.split(':')

    if clean_line.find("Time:") == 0:
        int_tokens = tokens[1].split()
        for tk in int_tokens:
            times.append(int(tk))

    if clean_line.find("Distance:") == 0:
        int_tokens = tokens[1].split()
        for tk in int_tokens:
            distances.append(int(tk))

# For each time, calculate the # of ways
# to beat the distance in the given time
answers = list()
for i in range(len(times)):
    T = float(times[i])
    D = float(distances[i])
    sqrt_part = math.sqrt(T*T-4.0*D)
    ans = list()
    ans.append((T + sqrt_part)/2.)
    ans.append((T - sqrt_part)/2.)
    sorted_ans = sorted(ans)
    n1 = math.floor(sorted_ans[0])
    while n1*(T-n1) <= D:
        n1 += 1
    n2 = math.floor(sorted_ans[1])
    while n2*(T-n2) <= D:
        n2 -= 1
    n = abs(n2-n1) + 1
    answers.append(n)

prod = 1
for ans in answers:
    prod *= ans
print(prod)