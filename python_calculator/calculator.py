# Python Calculator

def valid_float_input():
  while True:
    try:
      num_1 = float(input("First number: "))
      num_2 = float(input("Second number: "))
      return num_1, num_2
    except:
      print("Sorry but that is an invalid input.")
      print("Please enter a whole or decimal number to run the operation. Try again.\n")
      continue

def add():
  num_1,num_2 = valid_float_input() 
  sum = num_1 + num_2
  print("%d + %d = %d" % (num_1, num_2, sum))
  
def sub():
  num_1,num_2 = valid_float_input() 
  difference = num_1 - num_2
  print("%d - %d = %d" % (num_1, num_2, difference))

def mul():
  num_1,num_2 = valid_float_input() 
  product = num_1 * num_2
  print("%d x %d = %d" % (num_1, num_2, product))

def div():
  num_1,num_2 = valid_float_input() 
  quotient = num_1 / num_2
  print("%d / %d = %d" % (num_1, num_2, quotient))

def valid_operation_input():
  while True:
    try:
      option = int(input("Operation (Choose #): "))
      if option > 0 and option <= 4:
        return option
      else:
        print("Sorry but that is not a choice. Try again.\n")
        continue
    except ValueError:
      print("Sorry but that was not a number!\n")
      continue

def calculator(choice):
  if choice == 1:
    add()
  elif choice == 2:
    sub()
  elif choice == 3:
    mul()
  elif choice == 4:
    div()

def stay_on():
  keep_going = True
  user_input = ""
  while keep_going:
    calculator(valid_operation_input())
    while user_input.lower() != "n" or user_input.lower() != "y":
      user_input = input("Continue? (Y/N) ")
      if user_input.lower() == "y":
        break
      elif user_input.lower() == "n":
        print("Calculator shutting off...Good Bye....")
        keep_going = False
        break
      else:
        print("Invalid entry. Please try again.\n")
        continue

print("Welcome to the Python Calculator!")
print()
print("What operation would you like to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
stay_on()
