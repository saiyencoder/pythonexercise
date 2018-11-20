# Python Calculator

def add(num_1, num_2):
  return num_1 + num_2

def sub(num_1, num_2):
  return num_1 - num_2

def mul(num_1, num_2):
  return num_1 * num_2

def div(num_1, num_2):
  return num_1 / num_2


print("Welcome to the Python Calculator!")
print()
print("What operation would you like to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Operation (Choose #): "))

if operation == 1:
  num_1 = int(input("First number: "))
  num_2 = int(input("Second number: "))
  print("%d + %d = %d" % (num_1, num_2, add(num_1,num_2)))
elif operation == 2:
  num_1 = int(input("First number: "))
  num_2 = int(input("Second number: "))
  print("%d - %d = %d" % (num_1, num_2, sub(num_1,num_2)))
elif operation == 3:
  num_1 = int(input("First number: "))
  num_2 = int(input("Second number: "))
  print("%d x %d = %d" % (num_1, num_2, mul(num_1,num_2)))
elif operation == 4:
  num_1 = int(input("First number: "))
  num_2 = int(input("Second number: "))
  print("%d / %d = %d" % (num_1, num_2, div(num_1,num_2)))
