# Compress the String
# Send Feedback
# Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
# Example:
# If a string has 'x' repeated 5 times, replace this
# "xxxxx" with "x5".
# The string is compressed only when the repeated character count is more than 1.
# Note:
# Consecutive count of every character in the input string is less than or equal to 9. You are not required to print anything. It has already been taken care of.
# Just implement the given function and return the compressed string.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The output contains the string after compression printed in single line
# Constraints:
# 0 <= N <= 10^6
# Where 'N' is the length of the input string.
# Time Limit: 1 sec
# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa


def isPermutation(string1, string2) :
    dict1 ={}
    for x in string1:
        dict1[x] = dict1.get(x,0) +1
    for x in string2:
        if x in dict1 and dict1[x] > 0:
            dict1[x] = dict1[x] -1
        else:
            return False
    return sum([x for x in dict1.values()]) == 0

str1 = "race"
str2 = "rate"

print(isPermutation(str1,str2))