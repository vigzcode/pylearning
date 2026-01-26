text = "Hello, World!"
print(text)

text2 = 'Python is fun.'
print(text2)


print("""
This is a multi-line string.
      """)


for i in text:
    print(i)
print("Done iterating through the string.")

if 'H' in text:
    print("H is found in the string.")
else:
    print("H is not found in the string.")



"""
forward indexing:
0 : First character
1 : Second character
2 : Third character
"""
print("1st Character:", text[0])
print("2nd Character:", text[1])
print("3rd Character:", text[2])


"""
Reverse indexing:
-1 : Last character
-2 : Second last character
-3 : Third last character
"""

print("Last Character:", text[-1])
print("Second Last Character:", text[-2])
print("Third Last Character:", text[-3])



"""
string is immutable
values cannot be changed
Attempting to change a value will raise an error
for example:
text[0] = 'h'  # This will raise a TypeError
"""



"""
slicing syntax: string[start:end]
Includes characters from start index up to, but not including, end index
"""

print("Slicing from index 0 to 5:", text[0:5])  # Hello
print("Slicing from index 7 to 12:", text[7:12])  # World
print("Slicing from index 7 to end:", text[7:])
print("Slicing from start to index 5:", text[:5])



"""
String methods 
len - returns length of string
replace - replaces a substring with another substring
strip - removes leading and trailing whitespace
Upper - converts string to uppercase
lower - converts string to lowercase
split - splits string into a list based on a delimiter
"""

print("Length of text:", len(text))  # 13
new_text = text.replace("World", "Python")
print("After replacement:", new_text)  # Hello, Python!

whitespace_text = "   Hello, World!   "
print("Before strip:", repr(whitespace_text))
stripped_text = whitespace_text.strip()
print("After strip:", repr(stripped_text))  # 'Hello, World!'

upper_text = text.upper()
print("Uppercase text:", upper_text)  # HELLO, WORLD!

lower_text = text.lower()
print("Lowercase text:", lower_text)  # hello, world!


split_text = text.split(", ")
print("Split text:", split_text)  # ['Hello', 'World!']