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