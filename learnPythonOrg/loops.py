# There are 2 types of loop in Python, "for" and "while"
# For loops iterate over a given sequence.
primes = [2, 3, 5, 7]
for prime in primes:
  print(prime)

# For loops can iterate over a sequence using the "range" and "xrange" functions.
# Python 3 uses the range function, which acts like xrange. Range function is zero based.

# Prints out the numbers 0,1,2,3,4
for x in range(5):
  print(x)

# Prints out 3,4,5 ; Starts at 3 and stops at 6 but excludes it.
for x in range(3,6):
  print(x)

# Prints out 3,5,7 ; (starts,stops,step/skip)
for x in range(3,8,2):
  print(x)

# While loop repeat as long as a certain boolean condition is met.
# Prints out 0,1,2,3,4
count = 0
while count < 5:
  print(count)
  count +=1

# "break" and "continue" statements
# "break" is used to exit a for loop or a while loop, whereas "continue" is used to skip the current block, and return to the "for" or "while" statement
# Prints out 0,1,2,3,4
count = 0
while True:
  print(count)
  count += 1
  if count >= 5:
    break

# Prints out only the odd numbers
# If x is even, it will continue onto the next number
for x in range(10):
  if x % 2 == 0:
    continue
  print(x)