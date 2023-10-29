# Code : Interesting Alphabets
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE
# Input format :
# N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 26
# Sample Input 1:
# 8
# Sample Output 1:
# H
# GH
# FGH
# EFGH
# DEFGH
# CDEFGH
# BCDEFGH
# ABCDEFGH
n = int(input())
count = 65 + n - 1
r = n

while r > 0:
    c = n - r + 1
    d = count
    while c > 0:
        print(chr(d), end="")
        c -= 1
        d += 1
    print()
    r -= 1
    count -= 1
