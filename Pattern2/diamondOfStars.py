# Code : Diamond of stars
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

n = int(input())

r = n / 2
count = 1
while r > 0:
    # space
    s = r - 1
    while s > 0:
        print(" ", end="")
        s -= 1
    # stars
    d = count
    while d > 0:
        print("*", end="")
        d -= 1
    print()
    r -= 1
    count += 2

r = n - (n / 2) - 1
e = 1
count = n - 2
while r > 0:
    # space
    s = e
    while s > 0:
        print(" ", end="")
        s -= 1
    # stars
    d = count
    while d > 0:
        print("*", end="")
        d -= 1
    print()
    r -= 1
    e += 1
    count -= 2
