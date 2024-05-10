# Booleans

In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

``` python

print(10 > 9)
print(10 == 9)
print(10 < 9)

# OUT
True
False
False
```

## Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return


``` python

print(bool("Hello"))
print(bool(15))

# OUT
True
True
```

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

``` python

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# OUT
False
False
False
False
False
False
False
```

One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

``` python

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# OUT
False
```

Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

``` python

x = 200
print(isinstance(x, int))

# OUT
True
```