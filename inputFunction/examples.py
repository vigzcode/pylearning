name = input("Enter your name: ")
print("Hello,", name)
print(type(name))

age = int(input("Enter your age: ")) # Convert input to integer
print("Your age is:", age)
print(type(age))
print("Next year, you will be:", age + 1)
print(age + 1)

a, b = input("Enter two numbers: ").split()
print("You entered:", a, "and", b)

print(type(a))
print(type(b))


a, b = (int(x) for x in input("Enter two numbers: ").split())
a, b = map(int, input("Enter two numbers: ").split())
print("You entered:", a, "and", b)
print(type(a))
print(type(b))