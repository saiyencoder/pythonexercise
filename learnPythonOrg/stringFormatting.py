"""
Python uses C-style string formatting to create new, formatted strings.
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
"""

# This will print out "Fetch Cubby!"
dogName = "Cubby"
print("Fetch %s!" % dogName)

# To use two or more argument specifiers, use a tuple(parentheses)
age = 8
color = "white"
print("%s is %d years old." % (dogName,age))
print("%s is %s years old and has %s fur." % (dogName,age,color))

# Any object which is not a string can be formatted using the "%s" as well.
# This prints out: list: [1, 2, 3]
mylist = [1,2,3]
print("list: %s" % mylist)

"""
Some basic argument specifiers:

%s - String(or any object with a string representation, like numbers)
%d - Integers
%f - Floating pointnumbers
%.<number of digits>f - Floating point numbers with a fixed amoint of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
