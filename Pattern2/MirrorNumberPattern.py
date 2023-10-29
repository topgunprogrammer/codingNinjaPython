# Code : Mirror Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#
#
#
#
# The dots represent spaces.
#
#
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 3
# Sample Output 1:
#       1
#     12
#   123

n = int(input())
r = n
count = 1

while r > 0:
    c = n
    d = 1
    while c > 0:
        if c > count:
            print(" ", end="")
        else:
            print(d, end="")
            d += 1
        c -= 1

    print("")
    r -= 1
    count += 1
