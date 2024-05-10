# Strings

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
To check if a certain phrase or character is present in a string, we can use the keyword in.

``` python

txt = "The best things in life are free!"
print("expensive" not in txt)

# OUT
True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# OUT 
# Yes, 'free' is present.
```

### Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

``` python

txt = "The best things in life are free!"
print("expensive" not in txt)

# OUT 
True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# OUT
# No, 'expensive' is NOT present.  
```


### Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.



``` python

b = "Hello, World!"
print(b[2:5]) # o primeiro valor é incluido e o segundo é excluido

#OUT
#llo
```

### Slice From the Start
By leaving out the start index, the range will start at the first character:

``` python

b = "Hello, World!"
print(b[:5])

#OUT
Hello
```

### Slice To the End
By leaving out the end index, the range will go to the end:

``` python

b = "Hello, World!"
print(b[2:])
#OUT
llo, World!
```

### Negative Indexing
Use negative indexes to start the slice from the end of the string:

``` python

b = "Hello, World!"
print(b[-5:-2])
#OUT
orl
```

## Modify Strings

### Upper Case

``` python

a = "Hello, World!"
print(a.upper())

# OUT
# HELLO, WORLD!
```

### Lower Case

``` python

a = "Hello, World!"
print(a.lower())

# OUT
# hello, world!
```

### Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

``` python

a = "Hello, World!"
print(a.strip())

# OUT
# Hello, World!
```

### Replace String

``` python

a = "Hello, World!"
print(a.replace("H", "J"))

# OUT
# Jello, World!
```


### Split String
The split() method returns a list where the text between the specified separator becomes the list items.

``` python

a = "Hello, World!"
print(a.split(","))

# OUT
# ['Hello', ' World!']
```

## Format - Strings

### F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

``` python

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# OUT
# My name is John, I am 36
```

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

``` python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# OUT
# The price is 59.00 dollars
```

A placeholder can contain Python code, like math operations:

``` python

txt = f"The price is {20 * 59} dollars"
print(txt)

# OUT
# The price is 1180 dollars
```

## Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert

``` python

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# OUT
# txt = "We are the so-called "Vikings" from the north."
```

| Code  | Result |
| ------------- | ------------- |
| \'	| Single Quote	|
| \\	| Backslash	|
| \n	| New Line	|
| \r	| Carriage Return |
| \t	| Tab	|
| \b	| Backspace	|
| \f	| Form Feed	|
| \ooo	| Octal value	|
| \xhh	| Hex value|


## String Methods

**Note: All string methods return new values. They do not change the original string.**

[Link](https://www.w3schools.com/python/python_strings_methods.asp)
