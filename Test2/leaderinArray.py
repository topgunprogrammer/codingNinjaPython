# 6
# 3 12 34 2 0 -1
import sys

n = int(input())
li = [int(x) for x in input().split()]

li.reverse()

output =[]
max = -sys.maxsize -1

for x in li :
     if x >= max:
         output.append(x)
         max = x




output.reverse()
for x  in output:
    print(x ,end=" ")