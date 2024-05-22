# Array

Collection of item stored consecutively in the memory

- all items in a array have the same type
- had to have a fixed size

``` cpp
int numbers [3] {10, 59, 11};

string cars [3] {"BMW", "Volvo", "Ford"};

char types [3] {'A', 'B', 'C'};
``` 


## Arrays operations 
### Algorithmic complexities 


``` Javascript
const numbers = {5, 9, 1, 6, 2, 1, 3};

console.log(numbers[5]);//out 1

// ALGORITHMIC COMPLEXITY
o(1)

``` 


``` Javascript
const numbers = {5, 9, 1, 6, 2, 1, 3};

//INSERTING AT INDEX

//Algorithmic complexity 
O(n)

``` 

``` Javascript
const numbers = {5, 9, 1, 6, 2, 1, 3};

//DELETING FROM INDEX 

//Algorithmic complexity 
O(n)

``` 

``` Javascript
const numbers = {5, 9, 1, 6, 2, 1, 3};

//UPDATING AT INDEX

//Algorithmic complexity 
O(1)

``` 

``` Javascript
const numbers = {5, 9, 1, 6, 2, 1, 3};

//TRAVERSING THE INDEX

//Algorithmic complexity 
O(n)

``` 


# Arrays in python

**Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.**

**Também é possivel utilizar a biblioteca NUMPY ou o ARRAY**

## Arrays
**Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.**
Arrays are used to store multiple values in one single variable

``` py
cars = ["Ford", "Volvo", "BMW"]
``` 

## What is an Array?
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.

## Access the Elements of an Array
You refer to an array element by referring to the index number.

``` py
x = cars[0]
``` 

``` py
cars[0] = "Toyota"
``` 

## The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

``` py
x = len(cars)
```

## Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

``` py
for x in cars:
  print(x)
```

## Adding Array Elements
You can use the append() method to add an element to an array.
``` py
cars.append("Honda")
```

## Removing Array Elements
You can use the pop() method to remove an element from the array.
``` py
cars.pop(1)
```
You can also use the remove() method to remove an element from the array.

``` py
cars.remove("Volvo")
```

**Note: The list's remove() method only removes the first occurrence of the specified value.**

### Array Methods
Python has a set of built-in methods that you can use on lists/arrays.

|Method	| Description|
| ----- | ---------- |
|append()	| Adds an element at the end of the list|
|clear()	| Removes all the elements from the list|
|copy()	| Returns a copy of the list|
|count()	| Returns the number of elements with the specified value|
|extend()	| Add the elements of a list (or any iterable), to the end of the current list|
|index()	| Returns the index of the first element with the specified value|
|insert()	| Adds an element at the specified position|
|pop()	| Removes the element at the specified position|
|remove()	| Removes the first item with the specified value|
|reverse()	| Reverses the order of the list|
|sort()	| Sorts the list|


# What is an Array in Python?
An array is basically a data structure which can hold more than one value at a time. It is a collection or ordered series of elements of the same type.

``` py
a=arr.array('d',[1.2,1.3,2.3])
```

We can loop through the array items easily and fetch the required values by just specifying the index number. Arrays are mutable(changeable) as well, therefore, you can perform various manipulations as required.


Now, there is always a question that comes up to our mind –

## Is Python list same as an Array?
Python Arrays and lists are store values in a similar way. But there is a key difference between the two i.e the values that they store. A list can store any type of values such as intergers, strings, etc. An arrays, on the other hand, stores single data type values. Therefore, you can have an array of integers, an array of strings, etc.

Python also provide [Numpy Arrays](https://www.edureka.co/blog/python-numpy-tutorial/) which are a grid of values used in Data Science. You can look into [Numpy Arrays vs Lists](https://www.edureka.co/blog/python-numpy-tutorial/#NumpyVsList) to know more.

## Creating an Array in Python:
Arrays in Python can be created after importing the array module as follows –

→         import array as arr

The array(data type, value list) function takes two parameters, the first being the data type of the value to be stored and the second is the value list. The data type can be anything such as int, float, double, etc. Please make a note that arr is the alias name and is for ease of use. You can import without alias as well. There is another way to import the array module which is –

→         from array import *

This means you want to import all functions from the array module.

The following syntax is used to create an array.


``` py
a=arr.array(data type,value list) 
```

![alt text](image.png)

## Basic array operations :
There are many operations that can be performed on arrays which are as follows –

![alt text](image-1.png)

### Finding the Length of an Array
Length of an array is the number of elements that are actually present in an array. You can make use of len() function to achieve this. The len() function returns an integer value that is equal to the number of elements present in that array.

Syntax:

``` py
→ len(array_name)
``` 

Example:

``` py
a=arr.array('d', [1.1 , 2.1 ,3.1] )
len(a)
Output –  3
```

This returns a value of 3 which is equal to the number of array elements.

### Adding/ Changing elements of an Array:
We can add value to an array by using the append(), extend() and the insert (i,x) functions.

The append() function is used when we need to add a single element at the end of the array.


``` py
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)

#OUT
array(‘d’, [1.1, 2.1, 3.1, 3.4])

a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.extend([4.5,6.3,6.8])
print(a)

#OUT
array(‘d’, [1.1, 2.1, 3.1, 4.5, 6.3, 6.8])


a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.insert(2,3.8)
print(a)

#OUT
array(‘d’, [1.1, 2.1, 3.8, 3.1])

```


### Array Concatenation :

``` py
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
b=arr.array('d',[3.7,8.6])
c=arr.array('d')
c=a+b
print("Array c = ",c)
```



# NumPy 

## Python NumPy Operations

- ndim:
You can find the dimension of the array, whether it is a two-dimensional array or a single dimensional array. So, let us see this practically how we can find the dimensions. In the below code, with the help of ‘ndim’ function, I can find whether the array is of single dimension or multi dimension.

``` py
import numpy as np
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
Output – 2
```

Since the output is 2, it is a two-dimensional array (multi dimension).

- itemsize:
You can calculate the byte size of each element. In the below code, I have defined a single dimensional array and with the help of ‘itemsize’ function, we can find the size of each element.

- dtype:
You can find the data type of the elements that are stored in an array. So, if you want to know the data type of a particular element, you can use ‘dtype’ function which will print the datatype along with the size. In the below code, I have defined an array where I have used the same function.
 
 - reshape:
Reshape is when you change the number of rows and columns which gives a new view to an object. Now, let us take an example to reshape the below array: