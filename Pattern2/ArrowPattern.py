# Arrow pattern
# Send Feedback
# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Sample Input :
# 11
# Sample Output :
# *
#  * *
#    * * *
#      * * * *
#        * * * * *
#          * * * * * *
#        * * * * *
#      * * * *
#    * * *
#  * *
# *
n = 7  # int(input())

r = n / 2
space = 0
count = 1

while r > 0:
    # space
    b = space
    while b > 0:
        print(" ", end="")
        b -= 1
    # stars
    a = count
    while a > 0:
        print("* ", end="")
        a -= 1
    print()
    r -= 1
    count += 1
    space += 1

r = n - (n / 2)
space -= 2
count -= 2
while r > 0:
    # space
    b = space
    while b > 0:
        print(" ", end="")
        b -= 1
    # stars
    a = count
    while a > 0:
        print("* ", end="")
        a -= 1
    print()
    r -= 1
    space -= 1
    count -= 1
