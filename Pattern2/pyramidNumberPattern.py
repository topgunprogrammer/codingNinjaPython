# Pyramid Number Pattern
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines
#
# Sample Input :
# 5
# Sample Output :
#         1
#       212
#     32123
#   4321234
# 543212345

n = 4  # int(input())

r = n
space = n - 1
count = 1
d = 1
while r > 0:
    # space
    s = space
    while s > 0:
        print(" ", end="")
        s -= 1
    # num
    num = count
    e = d
    flag = True
    while e > 0:
        print(num, end="")
        if flag:
            if num == 1:
                flag = False
                num += 1
            else:
                num -= 1
        else:
            num += 1
        e -= 1
    print()
    r -= 1
    space -= 1
    count += 1
    d += 2
