
# print all prime numbers till N

# n = int(input())
# memo = [2,3]
# def printAllPrimes(n,memo):
#     i = 2
#     while i <= n :
#         flag = True
#         for num in memo:
#             if i%num ==0:
#                 flag = False
#                 break;
#
#         if flag :
#             memo.append(i)
#
#         i+=1;
#
#
# printAllPrimes(n,memo)
# memo.sort();
# print(memo)


# check if number is prime or not

n = 10067 #int(input())
memo = [2,3,5]

def isPrime(n) -> bool:
    i = 1
    count = 0
    while i <= n//2 :
        count +=1
        if i != 1 and n % i == 0:
            print(count, end=" ")
            return False
        i += 2
    print(count, end=" ")
    return True

output = isPrime(n)

print(output)








