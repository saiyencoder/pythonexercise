from random import randint

def random_num():
  return randint(1,100)


print("Welcome to the guessing game!\nTry to guess the number we are thinking.\nThe number is between 1 and 100\n")

num = random_num()
guessed_it = False
guess_count = 0

while guessed_it != True:
  try:
    guess = int(input("Your guess: "))
    guess_count += 1
    if guess < 1 or guess > 100:
      print("I clearly said between 1 and 100. Try again!")
    elif guess > num:
      print("Your guess is too high.")
    elif guess < num:
      print("Your guess is too low.")
    elif guess == num:
      print("You got it! CONGRATS!")
      guessed_it = True
  except:
    print("Sorry but that is an invalid entry! Try again...")

print("It took you {} guess(es) to get it right".format(guess_count))

