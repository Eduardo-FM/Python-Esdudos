```py
myset = {"apple", "banana", "cherry"}
```

## Set
Sets are used to store multiple items in a single variable.


A set is a collection which is unordered, unchangeable*, and unindexed.

**Note: Set items are unchangeable, but you can remove items and add new items.**

Sets are written with curly brackets.

```py
myset = {"apple", "banana", "cherry"}
```

**Note: Sets are unordered, so you cannot be sure in which order the items will appear.**

## Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

## Unordered
Unordered means that the items in a set do not have a defined order.

## Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

## Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

**Once a set is created, you cannot change its items, but you can remove items and add new items.**

## Duplicates Not Allowed
Sets cannot have two items with the same value.

```py
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#OUT
{'banana', 'cherry', 'apple'}
```

**Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:**

```py
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#OUT
{True, 2, 'banana', 'cherry', 'apple'}
```

**Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:**

```py
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#OUT
{False, True, 'cherry', 'apple', 'banana'}
```


## Get the Length of a Set
To determine how many items a set has, use the len() function.

```py
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#OUT
3
```

## type()
From Python's perspective, sets are defined as objects with the data type 'set':

> <class 'set'>

```py
myset = {"apple", "banana", "cherry"}

print(type(myset))

#OUT
<class 'set'>
```

## The set() Constructor
It is also possible to use the set() constructor to make a set.

```py
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.

#OUT
{'banana', 'apple', 'cherry'}
```
## Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

1. Loop through the set, and print the values:
```py
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#OUT
cherry
apple
banana
```
2. Check if "banana" is present in the set:
```py
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#OUT
True
```

3. Check if "banana" is NOT present in the set:
```py
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#OUT
False
```

# Add Set Items

## Add Items

Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.

```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#OUT
{'apple', 'orange', 'banana', 'cherry'}
```

## Add Sets
To add items from another set into the current set, use the update() method.

```py
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```

## Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

```py
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```

## Remove Item
To remove an item in a set, use the remove(), or the discard() method.

1. remove()
```py
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
```

2. discard()

```py
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

```

3. pop()

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

```py
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

```

4. clear()
The clear() method empties the set:

```py
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

```

5. del

```py
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists
```

## Loop Items
You can loop through the set items by using a for loop:

```py
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

# Join Sets

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

## Union
The union() method returns a new set with all items from both sets.

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# OUT
{'b', 'c', 'a', 2, 3, 1}
```

You can use the | operator instead of the union() method, and you will get the same result.

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


# OUT
{'b', 'c', 'a', 2, 3, 1}
```

## Join Multiple Sets
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# OUT
{John, 'a', 1, 'b', 2, 'c', 3, banana, apple, Elena, cherry}
```

When using the | operator, separate the sets with more | operators:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# OUT
{3, 1, 'b', banana, 'a', apple, 'c', 2, John, cherry, Elena}
```

## Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set.


```py
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# OUT
{'c', 'b', 3, 'a', 1, 2}
```

**Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.**

## Update
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# OUT
{3, 'a', 2, 'b', 'c', 1}
```

**Note: Both union() and update() will exclude any duplicate items.**

## Intersection
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# OUT
{'apple'}
```

You can use the & operator instead of the intersection() method, and you will get the same result.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# OUT
{'apple'}
```

**Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.**

The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

# OUT
{'apple'}
```

**The values True and 1 are considered the same value. The same goes for False and 0.**

## Difference
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

# OUT
{'banana', 'cherry'}
```

You can use the - operator instead of the difference() method, and you will get the same result.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# OUT
{'banana', 'cherry'}
```

**Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.**

1. difference_update()

The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

# OUT
{'banana', 'cherry'}
```

## Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# OUT

{'google', 'banana', 'microsoft', 'cherry'}
```

You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# OUT

{'google', 'banana', 'microsoft', 'cherry'}
```

**Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.**

The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

```py
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)

# OUT

{'google', 'banana', 'microsoft', 'cherry'}
```


# Set Methods

| Method |	Shortcut |	Description|
| ------ | --------- | ----------- |
|add()	 |	Adds an element to the set|
|clear()	| 	Removes all the elements from the set|
|copy()	 	Returns a copy of the set|
|difference()	| -	Returns a set containing the difference between two or more sets|
|difference_update()	| -=	Removes the items in this set that are also included in another, specified set|
| discard()	 |	Remove the specified item|
|intersection()	| &	Returns a set, that is the intersection of two other sets|
| intersection_update() |	&=	Removes the items in this set that are not present in other, specified set(s)|
| isdisjoint()	 	| Returns whether two sets have a intersection or not|
| issubset() | 	<=	Returns whether another set contains this set or not|
| 	|<	Returns whether all items in this set is present in other, specified set(s)|
|issuperset()	| >=	Returns whether this set contains another set or not|
| 	| >	Returns whether all items in other, specified set(s) is present in this set|
| pop()	 |	Removes an element from the set|
| remove()	 |	Removes the specified element|
| symmetric_difference() |	^	Returns a set with the symmetric differences of two sets|
| symmetric_difference_update()	| ^=	Inserts the symmetric differences from this set and another|
| union()	| \|	Return a set containing the union of sets|
| update()	| \|=	Update the set with the union of this set and others|