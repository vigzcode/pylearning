#Tuple Without Parentheses (Packing)
t = 1, 2, 3
print(t)

#Tuple With Parentheses
t2 = (6, 5, 4)
print(t2)


#Single Element Tuple (Note the comma)
t3 = (7,)
print(t3)

#Accessing Tuple Elements
print("First element of t:", t[0])
print("Second element of t2:", t2[1])

#Tuple Unpacking
a, b, c = t
print("Unpacked values from t:", a, b, c)
x, y, z = t2
print("Unpacked values from t2:", x, y, z)



#Nested Tuples
nested_t = (1, (2, 3), 4)
print("Nested tuple:", nested_t)


#Tuple Concatenation
concat_t = t + t2
print("Concatenated tuple:", concat_t)

#Tuple Repetition
repeated_t = t * 2
print("Repeated tuple:", repeated_t)

#Tuple Length
print("Length of t:", len(t))
print("Length of t2:", len(t2))

#Tuple Slicing
print("Slicing t from index 0 to 2:", t[0:2])
print("Slicing t2 from index 1 to end:", t2[1:])

# sort a tuple
unsorted_t = (3, 1, 4, 2)
sorted_t = tuple(sorted(unsorted_t))
print("Sorted tuple:", sorted_t)


#Iterating Through a Tuple
for item in t:
    print("Item in t:", item)


#Tuple Methods
print("Index of 2 in t:", t.index(2))
print("Count of 3 in t:", t.count(3))

#Immutability of Tuples
# The following line would raise an error if uncommented
# t[0] = 10  # This will raise a TypeError

