# s = "abcd"
# for c in s:
#     print(c, end=" ")
# ----------------------------------------------------------------
# a = 1
# b = 30
#
# if a % 3 == 0:
#     s = a
# elif a % 3 == 1:
#     s = a + 2
# else:
#     s = a + 1
#
# for c in range(s, b + 1, 3):
#     print(c, end=" ")
# ----------------------------------------------------------------
# for index, i in enumerate(range(1, 20)):
#     print(index, i)
# ----------------------------------------------------------------
# n = 4  # int(input())
# for i in range(1, n + 1, 1):
#     # spaces
#     for s in range(n - i):
#         print(" ", end="")
#     # increasing
#     for a in range(i, (2 * i), 1):
#         print(a, end="")
#     # decreasing
#     for b in range(2 * i - 2, i - 1, -1):
#         print(b, end="")
#     print()
# ----------------------------------------------------------------
i = 1
while i < 3:
    j = 0
    while j < 5:
        j = j + 1
        if j == 3:
            continue
        print(j, end="")
    i = i + 1
