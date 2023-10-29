# Print the pattern
# Send Feedback
# Print the following pattern for the given number of rows.
# Pattern for N = 5
#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines
#
# Sample Input :
# 4
# Sample Output :
#  1  2  3  4
#  9 10 11 12
# 13 14 15 16
#  5  6  7  8

n = 4  # int(input())


def create_2d_array(n):
    # Initialize a 2D array with zeros
    array = [[0 for _ in range(n)] for _ in range(n)]
    return array


def print_2d_array(array):
    for row in array:
        for element in row:
            print(element, end=' ')
        print()  # Move to the next row


list = create_2d_array(n)

r = 0
count = 1
toggle = True
top = 0
bottom = n - 1
while r < n:
    if toggle:
        i = top
        top += 1
        toggle = False
    else:
        i = bottom
        bottom -= 1
        toggle = True
    j = 0
    while j < n:
        list[i][j] = count
        count += 1
        j += 1
    r += 1

print_2d_array(list)
