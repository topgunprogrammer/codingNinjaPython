# Code : Reverse Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 5
# Sample Output 1:
# 1
# 21
# 321
# 4321
# 54321
n = int(input())
r = n
c = 1

while r > 0:
    c = n - r + 1
    while c > 0:
        print(c, end="")
        c -= 1
    print()
    r -= 1
