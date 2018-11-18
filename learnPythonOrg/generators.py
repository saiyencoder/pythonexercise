"""
 Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.
 """

from random import randint

def lottery():
  # returns 6 numbers between 1 and 40
  for i in range(6):
    yield randint(1,40)

  # returns a 7th number between 1 and 15
  yield randint(1,15)

for random_number in lottery():
  print("And the next number is... %d" % (random_number))

# This function decides how to generate the random numbers on its own, and executes the uield statements one at a time, pausing in vetween to yield execution back to the main loop.
