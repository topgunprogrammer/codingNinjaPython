# Array Sum
# Send Feedback
# Given an array of length N, you need to find and print the sum of all elements of the array.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# Sum
# Constraints :
# 1 <= N <= 10^6
# Note for C++:
# It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5.
# Sample Input :
# 3
# 9 8 9
# Sample Output :
# 26
n = int(input())
list = [int(x) for x in input().split()]
out = 0
for i in list:
    out += i

print(out)
