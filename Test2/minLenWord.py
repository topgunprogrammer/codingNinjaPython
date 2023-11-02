import sys

s =  input().split()
min = sys.maxsize
minword = ""
for x in s:
    if len(x) < min :
        minword = x
        min = len(x)

print(minword)