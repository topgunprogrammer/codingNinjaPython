# Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1

n = int(input())
r = n
c = n

while r > 0:
    c = r
    a = 1
    while c > 0:
        print(a, end="")
        c -= 1
        a += 1
    print()
    r -= 1
