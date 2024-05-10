A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case statements.

Python language doesn’t have a switch statement.

Python uses dictionary mapping to implement Switch Case in Python

```python
def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))
    
``` 