"""
1. Print e Comentários
Pergunta:
Escreva um programa que imprime "Olá, Mundo!" na tela. Adicione um comentário no código explicando o que ele faz.
"""

# print('Olá mundo!')
"""
O Código acima imprime 'Olá Mundo!'
"""

"""
2. Variáveis e Tipos de Dados

Crie variáveis para armazenar seu nome, idade, altura e se você é estudante (True/False). Imprima essas variáveis.
Verifique os tipos de cada variável usando a função type().
"""
# nome = "Eduardo Freitas Machado"
# idade = 25
# altura = 1.74
# estudande = True

# print(nome, idade, altura, estudande)
# print(type(nome))
# print(type(idade))
# print(type(altura))
# print(type(estudande))

"""
3. Operadores Aritméticos

Crie um programa que peça dois números ao usuário e imprima a soma, subtração, multiplicação e divisão desses números.
"""

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo numero: "))

#soma = numero1 + numero2
#subtracao = numero1 - numero2
#multiplicacao = numero1 * numero2
#divisao = numero1 / numero2

#print('Soma: ', soma)
#print('subtracao: ', subtracao)
#print('Multiplicação: ', multiplicacao)
#print('Divisao: ', divisao)

"""
4. Operadores de Comparação

Peça dois números ao usuário e imprima se o primeiro é maior, menor ou igual ao segundo.
"""

#print('Por favor digite dois números')
#numero1 = float(input('Número 1: '))
#numero2 = float(input('Número 2: '))

#if numero1 > numero2: 
    #print('Número 1 é maior que Número 2 ')
#elif numero1 < numero2:
#    print('Número 1 é menor que Número 2 ')
#else: 
    #print('Número 1 é igual que Número 2 ')

"""
5. Estruturas Condicionais

Escreva um programa que peça a idade do usuário e imprima uma mensagem diferente dependendo se ele é menor de idade, adulto ou idoso.
"""

"""
idade_do_usuario = int(input("Por favor, digite a sua idade! "))

if idade_do_usuario < 18:
    print('Você é menor de idade')
elif idade_do_usuario >= 18 and idade_do_usuario < 60:
    print('Você é adulto')
elif idade_do_usuario >= 60:
    print('Você é idoso')
"""


"""
6. Loops (For e While)

Use um loop for para imprimir os números de 1 a 10.
Use um loop while para imprimir os números de 1 a 10.

"""

"""
for i in range(1, 11):
    print(i)

a = 1
while (a < 11):
    print(a)
    a += 1
""" 

    
"""
7. Listas

Crie uma lista com 5 frutas e imprima a lista inteira e cada fruta individualmente.
Adicione uma fruta à lista e remova a primeira fruta da lista. Imprima a lista novamente.
"""
"""
frutas = ['banana', 'maçã', 'uva', 'pera', 'laranja']
print(frutas)

for fruta in frutas:
    print(fruta)

frutas.append('jabuticaba')
frutas.remove(frutas[0])
print(frutas)
"""

"""
8. Dicionários

Crie um dicionário com informações sobre uma pessoa (nome, idade, cidade). Imprima o dicionário.
Adicione uma nova chave-valor ao dicionário (por exemplo, "profissão") e imprima o dicionário atualizado.

"""
""""
pessoa = {'nome' : 'eduardo', 'idade' : 25, 'cidade' : 'Vila Velha'}
print(pessoa)
pessoa.update({'profissão': 'programador'})
print(pessoa)
"""

"""
9. Funções

Escreva uma função que recebe um nome e retorna uma saudação com esse nome.
Escreva uma função que recebe dois números e retorna a soma deles.
"""

"""
def imprimir_nome(nome):
    print(f'Olá {nome} seja bem vindo!')


def soma(a, b):
    return a + b


imprimir_nome("Eduardo")
print("Soma:", soma(5, 3))

"""

"""
10. List Comprehensions

Use list comprehension para criar uma lista com os quadrados dos números de 1 a 10.

"""

"""
numeros = [num for num in range(1, 11)]

print(numeros)
"""

"""
11. Manipulação de Strings

Peça ao usuário para digitar uma frase e imprima a frase em maiúsculas, minúsculas e com a primeira letra de cada palavra em maiúscula.
Peça ao usuário para digitar duas palavras e verifique se elas são anagramas.
"""


"""
12. Manipulação de Arquivos

Escreva um programa que cria um arquivo de texto, escreve algumas linhas de texto nele e depois lê e imprime o conteúdo do arquivo.

"""


"""
13 Módulos e Bibliotecas

Importe o módulo math e use pelo menos três funções diferentes dele (por exemplo, sqrt, pow, factorial).
"""


"""
14. Exceções

Escreva um programa que peça dois números ao usuário e divida o primeiro pelo segundo. Trate a exceção caso o usuário digite zero como segundo número.
"""
try: 
    num1 = float(input('Digite um numero '))
    num2 = float(input('Digite um numero '))
    divisao = num1 / num2
    print(divisao)
except ZeroDivisionError:
    print('impossível dividir um número por 0')

"""
15. Listas Aninhadas

Crie uma lista aninhada (matriz) de 3x3 e imprima cada elemento usando loops aninhados.
"""



"""
respostas 11 a 15
"""

"""
11. Manipulação de Strings
Pergunta:
Peça ao usuário para digitar uma frase e imprima a frase em maiúsculas, minúsculas e com a primeira letra de cada palavra em maiúscula. Peça ao usuário para digitar duas palavras e verifique se elas são anagramas.

Resposta:

python
Copiar código
# Solicitando uma frase ao usuário
frase = input("Digite uma frase: ")

# Imprimindo a frase em diferentes formatos
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Título:", frase.title())

# Verificando se duas palavras são anagramas
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sorted(palavra1) == sorted(palavra2):
    print(f"'{palavra1}' e '{palavra2}' são anagramas.")
else:
    print(f"'{palavra1}' e '{palavra2}' não são anagramas.")
12. Manipulação de Arquivos
Pergunta:
Escreva um programa que cria um arquivo de texto, escreve algumas linhas de texto nele e depois lê e imprime o conteúdo do arquivo.

Resposta:

python
Copiar código
# Criando e escrevendo em um arquivo
with open("arquivo_exemplo.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")

# Lendo e imprimindo o conteúdo do arquivo
with open("arquivo_exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
13. Módulos e Bibliotecas
Pergunta:
Importe o módulo math e use pelo menos três funções diferentes dele (por exemplo, sqrt, pow, factorial).

Resposta:

python
Copiar código
import math

# Usando funções do módulo math
print("Raiz quadrada de 16:", math.sqrt(16))
print("2 elevado a 3:", math.pow(2, 3))
print("Fatorial de 5:", math.factorial(5))
14. Exceções
Pergunta:
Escreva um programa que peça dois números ao usuário e divida o primeiro pelo segundo. Trate a exceção caso o usuário digite zero como segundo número.

Resposta:

python
Copiar código
# Solicitando números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Tentando dividir os números e tratando exceção
try:
    resultado = num1 / num2
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
15. Listas Aninhadas
Pergunta:
Crie uma lista aninhada (matriz) de 3x3 e imprima cada elemento usando loops aninhados.

Resposta:

python
Copiar código
# Criando uma lista aninhada (matriz) 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo cada elemento da matriz
for linha in matriz:
    for elemento in linha:
        print(elemento)
"""