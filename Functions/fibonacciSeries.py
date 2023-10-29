# Fibonacci Member
# Send Feedback
# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
# Note:
# Fibonacci series is the series of numbers where each number is obtained by adding two previous numbers. The first two numbers in the Fibonacci series are 0 and 1.
#
#
# Input Format :
# Integer N
# Output Format :
# true or false
# Constraints :
# 0 <= n <= 10^4
# Sample Input 1 :
# 5
# Sample Output 1 :
# true
def checkMember(n):
    a = 1
    b = 1
    while True:
        if a == n or b == n:
            return True
        elif a > n and b > n:
            return False
        a, b = b, a + b
    return False


n = int(input())
print("true" if checkMember(n) else "false")
