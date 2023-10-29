# Number Pattern 2
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003
# Input format :
# Integer N (Total no. of rows)
# Constraints:
# 1 <= n <= 50
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 202
# 3003
# 40004
n = int(input())
r = n
c = 1
d = 1
while r > 0:
    c = n - r + 1
    e = c
    while c > 0:
        if c == e or c == 1:
            print(d, end="")
        else:
            print(0, end="")
        c -= 1;
    print()
    r -= 1
    d = n - r
