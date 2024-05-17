
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

