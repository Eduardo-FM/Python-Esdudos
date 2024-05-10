import sys

print("Olá Mundo!")

# print(sys.version)  

''' 
stdout: A built-in file object that is analogous to the interpreter’s standard output stream in Python. 
stdout is used to display output directly to the screen console. 
Output can be of any form, it can be output from a print statement, an expression statement, and even a prompt direct for input. 
By default, streams are in text mode. In fact, wherever a print function is called within the code, it is first written to sys.stdout and then finally on to the screen. 
'''
# sys.stdout.write('Geeks')

# This code reads lines from the standard input until the user enters ‘q’. For each line, it prints “Input : ” followed by the line. Finally, it prints “Exit”.
''' 
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input: {line}')
print("Exit")
''' 

# Indentation
if 5 > 2:
    print("Five is greater then two")



# Variables
x = 5
y = "Hello, Word"


# Comments

#This is a comment.
print("Hello, World!")

'''
this is a comment
Ele é uma String de multipla linhas. Mas o python ignora String literals que não estão associadas a nenhuma variavel, então ele atua como string.
'''
