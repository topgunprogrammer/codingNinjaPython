# Fahrenheit to Celsius Function
# Send Feedback
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
# Note: You don't have to write the main function or take input. It has already been taken care of and you need to just print the integer value . Just write the code that prints Fahrenheit to Celsius table in the function itself.
# Input Format :
# 3 integers - S, E and W respectively
# Output Format :
# Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
# Constraints :
# 0 <= S <= 1000
# 0 <= E <= 1000
# 0 <= W <= 1000
# Sample Input 1:
# 0
# 100
# 20
# Sample Output 1:
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37

def printTable(s, e, w):
    while s <= e:
        c = int((s - 32) * (5 / 9))
        print(s, c)
        s += w


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)
