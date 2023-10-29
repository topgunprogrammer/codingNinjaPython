# Nth Fibonacci Number
# Send Feedback
# Write a program to find the Nth Fibonacci number using loops.
# Input Format :
# The first line of each test case contains a real number ‘N’.
# Output Format :
# For each test case, print its equivalent Fibonacci number.
# Constraints:
# 1 <= N <= 10000
# Where ‘N’ represents the number for which we have to find its equivalent Fibonacci number.
#
# Time Limit: 1 second
# Sample Input 1:
# 6
# Sample Output 1:
# 8
# Explanation
# The Fibonacci sequence starts with two numbers first number is 1 and second number is also 1. The subsequent numbers are found by adding the two preceding numbers. Therefore, the first six Fibonacci numbers are: 1, 1, 2, 3, 5, 8 . Hence, the 6th Fibonacci number is 8.


# print all values in fib
# a ,b = 1, 1
#
# count = 0
#
# n = int(input())
#
# while count < n :
#     print(a, end=" ")
#     a , b = b, a + b
#     count += 1

# print nth fib using while loop
# a ,b = 1, 1
#
# count = 0
#
# n = int(input())
#
# while count < n -1 :
#     a , b = b, a + b
#     count += 1
#
# print(a)

# print nth fib using recursive code
# n = int(input())
#
# def fib(n):
#     if n <=0:
#         return 0
#     if n == 1 or n==2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(n))

# print nth fib using recursive code + dynamic programming
n = int(input())
memo = {}
def fib(n):
    if n <=0:
        return 0
    if n == 1 or n==2:
        return 1
    if n in memo:
        return memo[n]
    memo[n-1] =  fib(n-1)
    memo[n-2] = fib(n-2)
    return   memo[n-1] +  memo[n-2]

print(fib(n))









