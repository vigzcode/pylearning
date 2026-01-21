age = 25
name = "John"
#Now we can use these values anywhere in the program.
print("Name:", name)
print("Age:", age)


# withOut using variables
print(10 + 10)
print(10 + 10)

#With variables
x = 10
print(x + x)
print(x + x)

print(5000 * 0.1)

# To make code more readable and maintainable
salary = 5000
tax_rate = 0.1
print(salary * tax_rate)


# To store the userInput
user_input = input("Enter your name: ")
print("Hello,", user_input)

# To Store Results of Computation
result = salary * tax_rate
print("Tax Amount:", result)


""" 
To Share Data Between Parts of Program
Variables allow: Functions, loops, and conditions, to work together by using sharing data.
"""

count = 0
for i in range(5):
    count += 1
print(count)


# To Change Value Dynamically
# Example: 
x = 10
x = "Hello"
x = 3.14

print(x)  # Output: 3.14