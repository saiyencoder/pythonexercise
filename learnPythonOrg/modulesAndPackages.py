"""
In programming, a module is a piece of software that has a specific functionality. For example, when building a ping pong game, one module would be responsible for the game logic, and another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited separately.

Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file. A Python module can have a set of functions, classes or variables defined and implemented. 

Ex. 
mygame/game.py
mygame/draw.py

The python script "game.py" will implement the game. It will use the function "draw_game" from the file "draw.py", or in other words, the "draw" module, that implements the logic for drawing the game on the screen.

Modules are imported from other modules using the "import" command.

Ex. (We are in "game.py")
# import the draw module
import draw

def play_game():
  ...

def main():
  result = play_game()
  draw.draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
  main()


# We can import a specific function from a module by using the "from" command.
from draw import draw_game # Now we dont have to use the dot notation(draw.draw_game) to use it

# We can also import all the objects using the "*" command.
from draw import *

# We can tell the Python interpreter to look for modules outside the local directory
PYTHONPATH=/foo python3 game.py
# This will execute "game.py", and will enable the script to load modules from the "foo" directory as well as the local directory.

# We can also run "sys.path.append("/foo")" as well.

*** Each package in Python is a directory which MUST contain a special file called "__init__.py" ***
*** This file can be empty, and it indicates that the directory it contains is a Python package. ***
*** So it can be imported the same way a module can be imported. ***
"""
