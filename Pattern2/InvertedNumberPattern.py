# Code : Inverted Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 333
# 22
# 1
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1:
# 5
# Sample Output 1:
# 55555
# 4444
# 333
# 22
# 1

n = int(input())

r = n
count = n
c = n

while r > 0:
    c = count
    while c > 0:
        print(count, end="")
        c -= 1
    print()
    r -= 1
    count -= 1
