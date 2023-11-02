# Triplet Sum
# Send Feedback
# You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
# Note :
# Given array/list can contain duplicate elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
#
# Third line contains an integer 'X'.
# Output format :
# For each test case, print the total number of triplets present in the array/list.
#
# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 50
# 0 <= N <= 10^2
# 0 <= X <= 10^9
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 12
# Sample Output 1:
# 5

# Function to find the count of triplets that sum up to the given value
from sys import stdin
def twoSum(arr,x) -> int:
    dict={}
    for item in arr:
        dict[item] = dict.get(item,0) +1
    count = 0
    for item in arr:
        required = x - item
        if required in dict and dict[required] > 0:
            if required == item:
                count += (dict[required] * dict[item]) -1
            else:
                count +=  (dict[required] * dict[item])
            dict[required] = 0
            dict[item] =0

    return count

def findTriplet(arr, n, x):
    numTriplets = 0
    for i in range(n):
        # for j in range((i + 1), n):
        #     for k in range((j + 1), n):
        #         if (arr[i] + arr[j] + arr[k]) == x:
        #             numTriplets += 1
        requiredTwoSum = x - arr[i]
        tempArr = arr.copy()
        tempArr.pop(i)
        two_count = twoSum(tempArr,requiredTwoSum)
        if two_count > 0 :
            numTriplets+=1
    return numTriplets


def takeInput():
    n = int(input())
    if n == 0:
        return list(), 0
    arr = list(map(int, input().strip().split(" ")))
    return arr, n


t = int(input().strip())
while t > 0:
    arr, n = takeInput()
    x = int(input().strip())
    print(findTriplet(arr, n, x))

    t -= 1
