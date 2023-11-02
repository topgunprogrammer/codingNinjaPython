# Wave Print
# Send Feedback
# +
# For a given two-dimensional integer array/list of size (N x
# M), print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.
# Input format:
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
# Second line onwards, the next 'N' lines or rows represent the ith row values.
# Each of the ith row constitutes 'M' column values separated by a single space.
# Output format :
# For each test case, print the elements of the two-dimensional array/list in the sine wave order in a single line, separated by a single space.
# Output for every test case will be printed in a seperate line.
# Constraints :
# 1<=t＜=10^2
# 0 <=N <= 10^3
# 0 <= M <= 1013
# Time Limit: 1sec
# Sample Input 1:
# 1
# 34
# 1234
# 5678
# 9 10 11 12
# Sample Output 1:
# 159106237111284


def wavePrint(mat, nRows, mCols):
    flag = True
    for col in range(mCols):
        if flag :
            for row in range(nRows):
                print(mat[row][col],end=" ")
            flag = False
        else:
            for row in range(nRows-1,-1,-1):
                print(mat[row][col], end=" ")
            flag = True




matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

wavePrint(matrix, len(matrix),len(matrix[0]))
