[article](https://learnpython.com/blog/python-match-case-statement/)

A basic implementation of match case statements looks a lot like an if statement in Python. If you need a refresher, we have an article on checking MULTIPLE CONDITIONS IN PYTHON WITH AN IF STATEMENT.

For those of you who have some background in other languages like Java or C, match case may look like a switch statement. Switch statements are functionally similar to if-else statements, but they require less code when defining the cases.

The match case statement in Python is more powerful and allows for more complicated pattern matching. Let’s start by looking at a basic example to demonstrate the syntax:

```python
>>> command = 'Hello, World!'
>>> match command:
...     case 'Hello, World!':
...         print('Hello to you too!')
...     case 'Goodbye, World!':
...         print('See you later')
...     case other:
...         print('No match found')
 
Hello to you too!
```

Here we define a variable command and use the match keyword to match it to the cases defined after each case keyword.  As a side note, match and case are better described as “soft” keywords, meaning they only work as keywords in a match case statement.  You can keep using “match” or “case” as a variable name in other parts of your program.  The case other is equivalent to else in an if-elif-else statement and can be more simply written as case _.

We’re using the print() function here to simply print text to the screen. But any other commands or function calls can go here to be executed if the case is matched.  We’ll see some more detailed examples below. If you want to learn more about the print() function, take a look at THIS ARTICLE.