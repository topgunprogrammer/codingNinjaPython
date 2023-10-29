# Number Pattern
# Send Feedback
# Print the following pattern for n number of rows.
# Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
# For eg. N = 5

n = 5  # int(input())
r = n
c = 2 * n
spaceLength = c - 2
count = 1

while r > 0:
    b = spaceLength
    e = count
    # number
    f = 1
    while e > 0:
        print(f, end="")
        e -= 1
        f += 1
    # space
    while b > 0:
        print(" ", end="")
        b -= 1
    # number
    f = count
    while f > 0:
        print(f, end="")
        f -= 1
    print()
    r -= 1
    spaceLength -= 2
    count += 1
