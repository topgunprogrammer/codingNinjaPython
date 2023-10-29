# Print Number Pyramid
# Send Feedback
# Print the following pattern for a given n.
# For eg. N = 6
# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456
# Sample Input 1 :
# 4
# Sample Output 1 :
# 1234
#   234
#     34
#       4
#     34
#   234
# 1234
n = 4  # int(input())
space = 0
i = 0
for r in range(0, n + (n - 1), 1):
    if r >= n - 1:
        i = space + 1
    else:
        i = r + 1
    s = space
    for c in range(0, n, 1):
        if s > 0:
            print(" ", end="")
            s -= 1
            continue
        print(i, end="")
        i += 1
    print()
    if r >= n - 1:
        space -= 1
    else:
        space += 1
