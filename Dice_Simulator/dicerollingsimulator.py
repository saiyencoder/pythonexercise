from random import randint

def roll_die(num_of_die,num_of_sides):
  counter = 1
  print("Results:")
  while counter < (num_of_die + 1) :
    print("Die {} rolled a {}".format(counter,randint(1,num_of_sides)))
    counter += 1
  
print("Welcome to the Dice Rolling Simulator!\n")

while True:
  try:
    num_of_die = int(input("How many die are you rolling? "))
    if num_of_die > 0:
      break
    else:
      print("Are you even rolling a die? Try again!\n")
  except:
    print("Sorry that is an invalid entry. Try again!\n")

while True:
  try:
    num_of_sides = int(input("How many sides does each die have? *A common die has 6 sides*\n# of sides: "))
    if num_of_sides >= 3:
      break
    else:
      print("I would LOVE to see a die that has less than 3 sides. Try again!\n")
  except:
    print("Sorry that is an invalid entry. Try again!\n")

print()
roll_die(num_of_die,num_of_sides)

