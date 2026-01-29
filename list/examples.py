numbers = [1, 2, 3, 4, 5]
data = ['apple', 'banana', 'cherry',10.5,True]
print(numbers)
print(data)

"""
printing particular item using indexing
"""
print(numbers[0]) 
# print(numbers[100]) # This will raise an IndexError. The index 100 is out of range for the list 'numbers' which has only 5 elements.
print("last item in the list:", data[-1])
print("second last item in the list:", data[-2])

"""
check if the particular item exists in the list
"""

if 'banana' in data:
    print("banana is found in the list")
else:
    print("banana is not found in the list")

"""
printing items using for loop
"""


for item in data:
    print(item)
print("Done iterating through the list.")



"""
Replacing Items:
Lists are mutable, so we can change their items.
For example, changing the first item in the 'numbers' list:
"""
numbers[0] = 10
print("Updated numbers list:", numbers)



numbers[0:3] = [20, 30, 40]
print("Updated numbers list after slicing assignment:", numbers)

numbers[1:4] = []
print("Updated numbers list after removing items using slicing:", numbers)



copy = numbers[:]
print("Copy of numbers list:", copy)



"""
Methods in Lists:
"""

print(len(numbers))


# concatenation
a = [3, 1, 4, 2, 5]
b = ['banana', 'apple', 'cherry']
c = a+ b
print(c)


# length of list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Length of data list:", len(data))
print("Length of numbers list:", len(numbers))


# append method
numbers.append(11)
print("Numbers list after append:", numbers)

# remove method
numbers.remove(5)
print("Numbers list after removing 5:", numbers)

# sort method
numbers.sort()
print("Sorted numbers list:", numbers)


# reverse method
numbers.reverse()
print("Reversed numbers list:", numbers)


# pop method
last_item = numbers.pop()
print("Popped item:", last_item)
print("Numbers list after pop:", numbers)


# insert method
numbers.insert(0, 100)
print("Numbers list after inserting 100 at index 0:", numbers)

# index method
index_of_3 = numbers.index(3)
print("Index of 3 in numbers list:", index_of_3)


# count method
count_of_2 = numbers.count(2)
print("Count of 2 in numbers list:", count_of_2)


# insert method
numbers.insert(0, 100)
print("Numbers list after inserting 100 at index 0:", numbers)



# clear method
numbers.clear()
print("Numbers list after clear:", numbers)


# del method
del numbers


