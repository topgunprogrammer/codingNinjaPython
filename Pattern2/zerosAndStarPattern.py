# Zeros and Stars Pattern
# Send Feedback
# Print the following pattern
# Pattern for N = 4
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000
# Input Format :
# N (Total no. of rows)
# Output Format :
# Pattern in N lines
# Sample Input 1 :
# 3
# Sample Output 1 :
# *00*00*
# 0*0*0*0
# 00***00

n = 3  # int(input())
r = n
zero = n - 1
x = 0
z = 0
while r > 0:
    # outer zero
    m = x
    while m > 0:
        print("0", end="")
        m -= 1
    print("*", end="")
    # zero
    y = zero
    while y > 0:
        print("0", end="")
        y -= 1
    print("*", end="")
    # zero
    y = zero
    while y > 0:
        print("0", end="")
        y -= 1
    print("*", end="")
    # outer zero
    m = z
    while m > 0:
        print("0", end="")
        m -= 1
    print()
    r -= 1
    x += 1
    z += 1
    zero -= 1
