# Code : Square Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 7
# Sample Output 1:
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
n = int(input())
r = n
c = n

while r >0 :
    c = n
    while c > 0:
        print(n, end="")
        c-=1
    print()
    r-=1
