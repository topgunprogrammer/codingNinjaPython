# Code : Triangular Star Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# *
# **
# ***
# ****
# Note : There are no spaces between the stars (*).
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 5
# Sample Output 1:
# *
# **
# ***
# ****
# *****
n = int(input())
r = n
c = 1

while r > 0:
    c = n - r + 1
    while c > 0:
        print("*", end="")
        c -= 1;
    print()
    r -= 1
