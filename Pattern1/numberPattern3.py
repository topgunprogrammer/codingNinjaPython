# Number Pattern 3
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 121
# 1221
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 121
# 1221
# 12221

n = int(input())
r = n
c = 1

while r > 0:
    c = n - r + 1
    e = c
    while c > 0:
        if c == e or c == 1:
            print(1, end="")
        else:
            print(2, end="")
        c -= 1;
    print()
    r -= 1
