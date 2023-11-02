# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

n = input().split()
row  = int(n[0])
col = int(n[1])
matrix = []
for _ in range(row):
    matrix.append([ int(x) for x in input().split() ] )


def printInPattern(row, n):
    for _ in range(n):
         for x in row :
             print(x, end=" ")
         print()

n = len(matrix)
for r in range(row):
    printInPattern(matrix[r], n)
    n -= 1