# Number Star pattern 1
# Send Feedback
# Print the following pattern for given number of rows.
# Input format :
# Integer N (Total number of rows)
# Output Format :
# Pattern in N lines
# Sample Input :
#    5
# Sample Output :
#  5432*
#  543*1
#  54*21
#  5*321
#  *4321

n = int(input())

r = n
s = 1

while r > 0:
    c = n
    while c > 0:
        if s == c:
            print("*", end="")
            c -= 1
            continue
        print(c, end="")
        c -= 1
    print()
    r -= 1
    s += 1
