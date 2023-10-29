# Number Pattern 1
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 111
# 1111
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 111
# 1111
# 11111
n = int(input())
r = n
c = 1

while r > 0:
    c = n - r + 1
    while c > 0:
        print(1, end="")
        c -= 1;
    print()
    r -= 1
