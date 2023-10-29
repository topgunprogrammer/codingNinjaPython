# Code : Star Pattern
# Send Feedback
# Print the following pattern
# Pattern for N = 4
#
#
#
# Hint
# As taught in the video, you just have to modify the code so that instead of printing numbers, it should output stars ('*').
# The dots represent spaces.
#
#
#
# Input Format :
# N (Total no. of rows)
# Output Format :
# Pattern in N lines
# Constraints :
# 0 <= N <= 50
# Sample Input 1 :
# 3
# Sample Output 1 :
#    *
#   ***
#  *****

n = int(input())
r = n
count = 1
d = 0
while r > 0:
    c = n
    while c > 0:
        if c > count:
            print(" ", end="")
        else:
            print("*", end="")
        c -= 1
    e = d
    while e > 0:
        print("*", end="")
        e -= 1
    print()
    r -= 1
    count += 1
    d += 1
