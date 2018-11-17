# Objects are an excapsulation of variables and functions into a single entity.
# Objects get their variables and functions classes.

# Basic Class
class MyClass:
  variable = "something"

  def function(self):
    print("This is a message from inside the class.")

# We then assign the above class(template) to an object.
# myObjectX holds an object of the class "MyClass" that contains the 
# variable and function defined within the class called "MyClass".
myObjectX = MyClass()

# Now to access the variable inside the newly created object "myObjectX", we use the dot notation.
print(myObjectX.variable) # outputs "something"

# We can create mulitple different objects that are the same class.
# However, each object contains independent copies of the variables defined in the class.

# Create a new object
myObjectY = MyClass()

myObjectY.variable = "pizza"

# Even though we changed the variable, the first object created will not have this change.
# Since the change was made in the second option, only the second object's variable will change.

print(myObjectX.variable) # Outputs "something"
print(myObjectY.variable) # Outputs "pizza"

# To access the function, we use the same notation as a variable.
myObjectX.function()