"""
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.(Hash)
Each value stored in a dictionary can be accessed using a key, which is any type of object(a string, a number, a list, etc.) instead of using its index to address it.
"""
# We will create a phonebook dictionary.
# It will contain the contact and number.
marvelsPhonebook = {}
marvelsPhonebook["Steve"] = 1234567890
marvelsPhonebook["Tony"] = 9203194201
marvelsPhonebook["Peter"] = 7654832109
print(marvelsPhonebook) # Output is {'Steve': 1234567890, 'Tony': 9203194201, 'Peter': 7654832109}

# We can also initialize a dictionary.
dcPhonebook = {
    "Clark": 8293453029,
    "Bruce": 1512327642,
    "Barry": 1431242154
}
print(dcPhonebook) # Output is {'Clark': 8293453029, 'Bruce': 1512327642, 'Barry': 1431242154}

# Dictionaries can be iterated over, just like a list.
# However, a dictionary, unlike a list, does not keep the order of the values stored in it.

for name, number in marvelsPhonebook.items():
  print("Phone number for %s is %d" % (name,number))

# To remove a specified index, we use the "del" keyword.
# del marvelsPhonebook["Steve"] would delete Steve's entry.
# Or we can use the pop() method as well
# dcPhonebook.pop("Bruce") will remove Bruce's entry
