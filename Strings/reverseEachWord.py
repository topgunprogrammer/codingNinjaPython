# Reverse Each Word
# Send Feedback
# Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed. A word is a combination of characters without any spaces.
# Example:
# Input Sentence: "Hello I am Aadil"
# The expected output will print, "olleH I ma lidaA".
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces. The input string represents the sentence given to Aadil.
# Output Format:
# The only line of output prints the sentence(string) such that each word in the sentence is reversed.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.
#
# All the words in string are separated by a single space.
#
# String does not contain any leading or trailing spaces.
#
# Time Limit: 1 second
# Sample Input 1:
# Welcome to Coding Ninjas
# Sample Output 1:
# emocleW ot gnidoC sajniN


def reverseEachWord(string) :
    str = ""
    for word in string.split():
        str = str +" "+ word[::-1]
    return str.strip()





str ="Welcome to Coding Ninjas"
print(reverseEachWord(str))