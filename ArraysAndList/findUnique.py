# Find Unique
# Send Feedback
# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.
#  Note:
# Unique element is always present in the array/list according to the given condition.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the unique element present in the array.
#
# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1

arr = [3,1,4,3,4]

dict = {}

for x in arr:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

for key, value in dict.items():
    if value  == 1 :
        print(key)