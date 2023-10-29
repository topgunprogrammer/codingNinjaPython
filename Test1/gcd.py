# Greatest Common Divisor
# Send Feedback
# You are given two numbers, ‘X’ and ‘Y’. Your task is to find the greatest common divisor of the given two numbers.
# The Greatest Common Divisor of any two integers is the largest number that divides both integers.
# For Example:
# You are given ‘X’ as 20 and ‘Y’ as 15. The greatest common divisor, which divides both 15 and 20, is 5. Hence the answer is 5.
# Input Format:
# The first line of input contains ‘T’, representing the number of test cases.
#
# The first line of each test case contains two space-separated integers, ‘X’ and ‘Y’, representing the given numbers.
# Output Format:
# For each test case, print a single integer representing the Greatest Common Divisor of ‘X’ and ‘Y’.
#
# Print a separate line for each test case.
# Note (c++, python):
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Constraints:
# 1 <= T <= 10
# 1 <= X, Y <= 10^9
# Sample Input 1:
# 2
# 20 15
# 8 32
# Sample Output 1:
# 5
# 8

import math


def findGcd(x, y):
    return math.gcd(x, y)
