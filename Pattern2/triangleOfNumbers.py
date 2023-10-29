# Code : Triangle of Numbers
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 4
#
#
#
# The dots represent spaces.
#
#
#
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1:
# 5
# Sample Output 1:
#            1
#           232
#          34543
#         4567654
#        567898765

n = int(input())

r = n
count = 1
num = 1
while r > 0:
    # print spaces
    s = n - count
    while s > 0:
        print(" ", end="")
        s -= 1
    # print numbers
    d = num
    e = count
    f = num // 2
    while d > 0:
        print(e, end="")
        if d - 1 <= f:
            e -= 1
        else:
            e += 1
        d -= 1

    print()
    r -= 1
    count += 1
    num += 2
