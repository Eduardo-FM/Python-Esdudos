# Dictionaries

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

# Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

# Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

## Ordered or Unordered?
> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

## Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

## Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

## Dictionary Length
To determine how many items a dictionary has, use the len() function:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "fabrication": 1964,
  "year": 2020
}
print(len(thisdict))


#OUT
4
```

## Dictionary Items - Data Types
The values in dictionary items can be of any data type

## type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict'

## The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

## Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

#OUT
Mustang
```

There is also a method called get() that will give you the same result:

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))

#OUT
Mustang
```

## Get Keys
The keys() method will return a list of all the keys in the dictionary.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)

#OUT
dict_keys(['brand', 'model', 'year'])
```

The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#OUT
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
```

## Get Values
The values() method will return a list of all the values in the dictionary.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)

#OUT
dict_values(['Ford', 'Mustang', 1964])
```

The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

## Get Items
The items() method will return each item in a dictionary, as tuples in a list.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


#OUT
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.


```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#OUT
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

```

## Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#OUT
Yes, 'model' is one of the keys in the thisdict dictionary
```

## Change Values
You can change the value of a specific item by referring to its key name:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
```

## Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

## Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

## Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

## Removing Items
There are several methods to remove items from a dictionary:

The **pop()** method removes the item with the specified key name:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#OUT
{'brand': 'Ford', 'year': 1964}
```

The **popitem()** method removes the last inserted item (in versions before 3.7, a random item is removed instead):

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#OUT
{'brand': 'Ford', 'model': 'Mustang'}
```
The **del** keyword removes the item with the specified key name:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#OUT
{'brand': 'Ford', 'year': 1964}
```

The del keyword can also delete the dictionary completely


The **clear()** method empties the dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#OUT
{}
```

## Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

```python
"""
Print all key names in the dictionary, one by one:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#OUT
brand
model
year
```

```python
"""
Print all values in the dictionary, one by one:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])


#OUT
Ford
Mustang
1964
```

```python
"""
You can also use the values() method to return values of a dictionary:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)


#OUT
Ford
Mustang
1964
```

```python
"""
You can use the keys() method to return the keys of a dictionary:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#OUT
brand
model
year
```

```python
"""
Loop through both keys and values, by using the items() method:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


#OUT
brand Ford
model Mustang
year 1964
```

## Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

Another way to make a copy is to use the built-in function dict().

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#OUT
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

## Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#OUT
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
```

Or, if you want to add three dictionaries into a new dictionary:

```python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#OUT
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
```

## Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#OUT
Tobias
```

## Loop Through Nested Dictionaries
You can loop through a dictionary by using the items() method like this:

```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

#OUT
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
```

#################################################################################
```python

#OUT
```

## Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

|Method	 | Description|
| ------ | ----------- |
|clear() |	Removes all the elements from the dictionary
|copy()	| Returns a copy of the dictionary
|fromkeys() |	Returns a dictionary with the specified keys and value
|get()	| Returns the value of the specified key
|items() |	Returns a list containing a tuple for each key value pair
|keys() |	Returns a list containing the dictionary's keys
|pop() |	Removes the element with the specified key
|popitem() |	Removes the last inserted key-value pair
|setdefault() |	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
|update() |	Updates the dictionary with the specified key-value pairs
|values() |	Returns a list of all the values in the dictionary