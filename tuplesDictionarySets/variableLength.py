# def sum(a,b):
#     return a+b
#
#
# print(sum(1,2))



def sum1(a,b , *more ):
    l = list(more)
    return a +b+ sum(l)


print(sum1(1,2,3,4,5,6))