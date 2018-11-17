"""
Lists are very similar to arrays.
They can contain any type of variable, and they can contain as many variables as you wish.
Lists can also be iterated over.
"""
mylist = []
mylist.append(1) # Adds 1 to the list
mylist.append(2) # Adds 2 to the end of the list
mylist.append(3) # Adds 3 to the end of the list
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3 (in their own line)
for x in mylist:
  print(x)

# Accessing an index out of range will throw an exception(an error)
# The following will throw a 'IndexError: list index out of range'
# print(mylist[10])






