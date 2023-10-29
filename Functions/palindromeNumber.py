# Palindrome number
# Send Feedback
# Check whether a given number ’n’ is a palindrome number.
# Note :
# Palindrome numbers are the numbers that don't change when reversed.
# You don’t need to print anything. Just implement the given function.
# Example:
# Input: 'n' = 51415
# Output: true
# Explanation: On reversing, 51415 gives 51415.
# Input Format:
# The first and only line of the input contains the number 'n'.
# Output format:
# Return a boolean value True or False.
# Sample Input 1 :
# 1032
# Sample Output 1 :
# false
# Explanation Of Sample Input 1:
# 1032, on being reversed, gives 2301, which is a totally different number.

n = int(input())


def isPalindrome(n) -> bool:
    return str(n) == str(n)[::-1]


print("true" if isPalindrome(n) else "false")
