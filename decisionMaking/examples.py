num1 = int(input("Enter a nominator: "))
num2 = int(input("Enter a denominator: "))

if num2 != 0:
    result = num1 / num2
    print("Result:", result)



"""
if else example
"""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


"""
if elif else example
"""

num = int(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")
