# Simple print
print("Hello Python")


# Multiple values
a = 10
b = 20
print("Values:", a, b)
print("Python", "is", "fun")   

# Custom separator
print("Apple", "Banana", "Cherry", sep=" | ")
print("Python", "is", "fun", sep="-")  

# No newline
print("Hello", end=" ")
print("World")

print("Loading" , end="...")

"""
You will see different behavior for the "Loading..." output because of the `end` parameter.
Since no newline is printed, the output depends on how the shell handles buffering.

In the zsh terminal:
   Output appears as: Loading...%
   (zsh flushes the output and shows `%` to warn that the line did not end with a newline)

In the bash terminal:
  "Loading..." may not appear at all
   (because stdout is fully buffered and, without a newline or flush, Python output
    may never be written before the program exits)
"""

# Redirect output to file
with open("output.txt", "w") as f:
    print("Hello File", file=f)
