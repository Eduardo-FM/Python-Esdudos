x = 5
y = "John"
print(x, y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

# Variable Names

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

#Legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Ilegal
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
print("Unpack a Collection")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
print("Output Variables")
x = "Python is awesome"
print(x)

# you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

print("-------------------------------------------------------------------------------------------------------------------------------------")

#Global Variables
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
print("Global Variables")

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("-------------------------------------------------------------------------------------------------------------------------------------")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("-------------------------------------------------------------------------------------------------------------------------------------")
# The global Keyword
print("The global Keyword")
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

x = 0

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


print("-------------------------------------------------------------------------------------------------------------------------------------")
print("Data Types")








