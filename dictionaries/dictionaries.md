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

```python


#OUT
```