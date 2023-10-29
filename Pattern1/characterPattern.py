# Code : Character Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 13
# Sample Input 1:
# 5
# Sample Output 1:
# A
# BC
# CDE
# DEFG
# EFGHI

n = int(input())
count = 65
r = n

while r > 0:
    c = n - r + 1
    d = count
    while c > 0:
        print(chr(d), end="")
        c -= 1
        d += 1
    print()
    r -= 1
    count += 1
