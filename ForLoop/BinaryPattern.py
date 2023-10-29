# Binary Pattern
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 1111
# 000
# 11
# 0
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines
#
# Sample Input :
# 5
# Sample Output :
# 11111
# 0000
# 111
# 00
# 1

n = int(input())
toggle = True

for r in range(0, n, 1):
    for c in range(0, n - r, 1):
        if toggle:
            print(1, end="")
        else:
            print(0, end="")
    print()
    toggle = not (toggle)
