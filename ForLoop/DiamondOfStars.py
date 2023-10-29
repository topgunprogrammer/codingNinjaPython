# Diamond of Stars
# Send Feedback
# Print the following pattern for the given number of rows.
# Note: N is always odd.
#
#
# Pattern for N = 5
#
#
#
# The dots represent spaces.
#
#
#
# Input format :
# N (Total no. of rows and can only be odd)
# Output format :
# Pattern in N lines
# Constraints :
# 1 <= N <= 49
# Sample Input 1:
# 5
# Sample Output 1:
#   *
#  ***
# *****
#  ***
#   *

n = 5  # int(input())

r = n
half = n // 2 + 1
c = half
space = c - 1
while r > 0:
    s = space
    a = c
    while a > 0:
        if s > 0:
            print(" ", end="")
            s -= 1
            a -= 1
            continue
        print("*", end="")
        a -= 1
    print()
    r -= 1
    if n - r >= half:
        space += 1
        c -= 1
    else:
        space -= 1
        c += 1
