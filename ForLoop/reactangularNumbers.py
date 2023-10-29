# Rectangular numbers
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines
#
# Sample Input :
# 3
# Sample Output :
# 33333
# 32223
# 32123
# 32223
# 33333
MAX = 100


# function to Print pattern
def prints(a, size):
    for i in range(size):
        for j in range(size):
            print(a[i][j], end='')
        print()


# function to compute pattern
def innerPattern(n):
    # Pattern Size
    size = 2 * n - 1
    front = 0
    back = size - 1
    a = [[0 for i in range(MAX)]
         for i in range(MAX)]
    while (n != 0):
        for i in range(front, back + 1):
            for j in range(front, back + 1):
                if (i == front or i == back or
                        j == front or j == back):
                    a[i][j] = n
        front += 1
        back -= 1
        n -= 1
    prints(a, size);


# Driver code

# Input
n = 4

# function calling
innerPattern(n)
