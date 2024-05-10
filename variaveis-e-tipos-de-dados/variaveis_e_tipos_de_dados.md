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

'''
Python has the following data types built-in by default, in these categories:

    Text Type: -> str
    Numeric Types: -> int, float, complex
    Sequence Types: -> list, tuple, range
    Mapping Type: -> dict
    Set Types: -> set, frozenset
    Boolean Type: -> bool
    Binary Types: -> bytes, bytearray, memoryview
    None Type: -> NoneType
'''

# Pegar o tipo de dado

x = 5
print(type(x))

# Setting the Data Type
print('Setting the Data Type')
#In Python, the data type is set when you assign a value to a variable:
'''
Example	Data                                    Type
x = "Hello World"	                              str	
x = 20	                                        int	
x = 20.5	                                      float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]             	list	
x = ("apple", "banana", "cherry")	              tuple	
x = range(6)	                                  range	
x = {"name" : "John", "age" : 36}             	dict	
x = {"apple", "banana", "cherry"}	              set	
x = frozenset({"apple", "banana", "cherry"})	  frozenset	
x = True	                                      bool	
x = b"Hello"	                                  bytes	
x = bytearray(5)	                              bytearray	
x = memoryview(bytes(5))	                      memoryview	
x = None	                                      NoneType	
'''

# Setting the Specific Data Type
'''
Example	Data                                      Type	
x = str("Hello World")	                          str	
x = int(20)	                                      int	
x = float(20.5)                                  	float	
x = complex(1j)                                  	complex	
x = list(("apple", "banana", "cherry"))           list	
x = tuple(("apple", "banana", "cherry"))	        tuple	
x = range(6)                                    	range	
x = dict(name="John", age=36)                   	dict	
x = set(("apple", "banana", "cherry"))          	set	
x = frozenset(("apple", "banana", "cherry"))    	frozenset	
x = bool(5)                                     	bool	
x = bytes(5)                                     	bytes	
x = bytearray(5)                                	bytearray	
x = memoryview(bytes(5))                        	memoryview
'''


print("-------------------------------------------------------------------------------------------------------------------------------------")

## Python Numbers
There are three numeric types in Python:

- int
- float
- complex

### Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

### Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Float can also be scientific numbers with an "e" to indicate the power of 10.

``` python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# OUT

<class 'float'>
<class 'float'>
<class 'float'>
```

Sendo feito a multiplicação do numero

``` python
x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)

# OUT

35000.0
120000.0
-8.77e+101
```

### Complex
Complex numbers are written with a "j" as the imaginary part:

``` python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

### Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

``` python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# OUT
1.0
2
(1+0j)
<class 'float'>
<class 'int'>
<class 'complex'>
```

### Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

``` python
import random

print(random.randrange(1, 10))
```

### Casting

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


## Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

``` python
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

### Multiline Strings
You can assign a multiline string to a variable by using three quotes, Or three single quotes::

``` python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

```

**Strings are Arrays**

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

``` python

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

```


### Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

``` python

for x in "banana":
  print(x)


# OUT 
b
a
n
a
n
a
```

### String Length
To get the length of a string, use the len() function.

``` python

a = "Hello, World!"
print(len(a))

# OUT 
13
```

### Check String
