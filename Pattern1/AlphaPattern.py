# Alpha Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 3
#  A
#  BB
#  CCC
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 26
# Sample Input 1:
# 7
# Sample Output 1:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# GGGGGGG

n = int(input())
count = 65
r = n

while r > 0:
    c = n - r + 1
    while c > 0:
        print(chr(count), end="")
        c -= 1
    print()
    r -= 1
    count += 1
