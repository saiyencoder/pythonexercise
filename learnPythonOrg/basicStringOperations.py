# The len() function will print out how many characters a string has
# Empty spaces and punctuation count as a character.
print(len("Hello World!")) # outputs 12

# We can find which index a letter/character is located at.
# Using the index() function will retrieve the first occurence of the character. 
string = "basketball"
print(string.index("b")) # outputs 0
print(string.index("e")) # outputs 4

# The count() function will count how many characters are located in the string
print(string.count("b")) # outputs 2
print(string.count("a")) # outputs 2

# We can print a slice of a string.
# string[startIndex:endIndex] : endIndex is excluded.
print(string[3:5]) # outputs "ke"
# string[Index] will return the single character at that index
print(string[4]) # outputs "e"
# string[:endIndex] will return the string from the beginning to the endIndex
print(string[:5]) # outputs "baske" excludes endIndex
# string[startIndex:] will return the string from the startIndex to the end of the string.
print(string[5:]) # outputs "tball"
# Entering a negative number inside the brackets will make it start at the end of the string. 
print(string[-3]) #outputs "a": 3rd character from the end
# There is also an extended slice syntax.
# string[start:stop:step] this will slice the string starting at "start" until the "stop" index skipping every "step" amount
print(string[1:8:2]) # outputs "akta"
# We can easily reverse a string with string[::-1]
print(string[::-1]) # outputs "llabteksab"
# We can make all characters in a string uppercase using upper()
print(string.upper()) # outputs "BASKETBALL"
# We can make all characters in a string lowercase using lower()
print(string.lower()) # outputs "basketball"
# We can check to see if a string starts or ends with something
print(string.startswith("basket")) #outputs true
print(string.startswith("foot")) #outputs false
print(string.endswith("ball")) #outputs true
print(string.endswith("ccer")) #outputs false
# We can split a string up using split("delimiter"). 
# It will split where it finds the delimiter
print(string.split("b")) # Output ["","asket","all"] since it splits when it finds the letter "b"


