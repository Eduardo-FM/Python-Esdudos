
``` py
mytuple = ("apple", "banana", "cherry")
```

Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

## Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

## Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

## Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

## Allow Duplicates
Since tuples are indexed, they can have items with the same value

## Tuple Length
To determine how many items a tuple has, use the len() function:

``` py
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#OUT
3
```

## Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

``` py
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#OUT
<class 'tuple'>
<class 'str'>
```

## The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

``` py
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


#OUT
('apple', 'banana', 'cherry')
```

## Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

``` py
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#OUT
banana
```

## Negative Indexing
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.

## Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

**Note: The search will start at index 2 (included) and end at index 5 (not included).**

Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item.

``` py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])
)

#OUT

('apple', 'banana', 'cherry', 'orange')
```

By leaving out the end value, the range will go on to the end of the tuple:

``` py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:])

#OUT

('cherry', 'orange', 'kiwi', 'melon', 'mango')
```

## Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:

``` py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

#OUT
('orange', 'kiwi', 'melon')

```

Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:

``` py
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#OUT
Yes, 'apple' is in the fruits tuple

```

# Update Tuples

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.

## Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

``` py
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#OUT
("apple", "kiwi", "cherry")

```

## Add Items
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

``` py
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#OUT
('apple', 'banana', 'cherry', 'orange')

```

2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

``` py
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#OUT
('apple', 'banana', 'cherry', 'orange')

```

## Remove Items
**Note: You cannot remove items in a tuple.**

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

1. Convert the tuple into a list, remove "apple", and convert it back into a tuple:
``` py
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#OUT
('banana', 'cherry')

```

2. Or you can delete the tuple completely:

The del keyword can delete the tuple completely

``` py
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#OUT
Traceback (most recent call last):
  File "demo_tuple_del.py", line 3, in <module>
    print(thistuple) #this will raise an error because the tuple no longer exists
NameError: name 'thistuple' is not defined

```

# Unpack Tuples

## Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

``` py
fruits = ("apple", "banana", "cherry")

#OUT
('apple', 'banana', 'cherry')

```

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

``` py
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#OUT
apple
banana
cherry

```

**Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.**

## Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

``` py
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#OUT
apple
banana
['cherry', 'strawberry', 'raspberry']

```

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

``` py
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#OUT
apple
['mango', 'papaya', 'pineapple']
cherry

```

## Loop Through a Tuple
You can loop through the tuple items by using a for loop.

``` py
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

## Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

``` py
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

## Using a While Loop
You can loop through the tuple items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

``` py
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

```

# Join Tuples

## Join Two Tuples
To join two or more tuples you can use the + operator:

``` py
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# OUT 
('a', 'b', 'c', 1, 2, 3)
```

## Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

``` py
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# OUT 
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

## Tuple Methods
Python has two built-in methods that you can use on tuples.

| Method	| Description |
| --------  | ----------- |
|count()	|Returns the number of times a specified value occurs in a tuple|
|index()	|Searches the tuple for a specified value and returns the position of where it was found|