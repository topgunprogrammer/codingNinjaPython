# Yet another Pattern
# Send Feedback
# Ninja was playing with her sister to solve a puzzle pattern. However, even after taking several hours, they could not solve the problem.
# A value of N is given to them, and they are asked to solve the problem. Since they are stuck for a while, they ask you to solve the problem. Can you help solve this problem?
# Example : Pattern for N = 4
#
# ****
#  ***
#   **
#    *
# Input Format:
# The first line of input contains an integer ‘T,’ denoting the number of test cases. The test cases follow.
#
# The first line of each test case contains a single integer ‘N’.
# Output Format:
# For each test case, print 'N' strings corresponding to every row in a new line (row elements not separated by space)
#
# Print the output of each test case in a separate line.
# Note (c++ ,Python):
# You are not required to print the expected output; it has already been taken care of. Just implement the function.
# Constraints:
# 1 <= T <= 50
# 1 <= N <= 300
#
# Time Limit: 1 sec
# Sample Input 1:
# 2
# 3
# 2
# Sample Output 1:
# ***
#  **
#   *
#
# **
#  *
def ninjaPuzzle(n):
    list = []
    for _ in range(n):
        list.append(int(input()))

    for i in list:
        printInvertedPyramid(i)
        print()


def printInvertedPyramid(n):
    r = n
    s = 0
    while r > 0:
        c = n
        a = s
        while c > 0:
            if a > 0:
                print(" ", end="")
                c -= 1
                a -= 1
                continue
            print("*", end="")
            c -= 1
        print()
        r -= 1
        s += 1


n = int(input())
ninjaPuzzle(n)
