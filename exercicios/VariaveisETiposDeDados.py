# Crie uma variável chamada `nome` e atribua a ela seu nome. Em seguida, imprima a variável.
print('Questão 1')
nome = 'eduardo'
print(nome)

print("-------------------------------------------------------------------")
# Crie variáveis chamadas `idade` e `altura` e atribua a elas sua idade e altura. Imprima ambas as variáveis.
print('Questão 2')
idade = 25
altura = 1.74
print('Idade: ', idade)
print('Altura: ', altura)
print("-------------------------------------------------------------------")

# Crie uma variável chamada `preco` e atribua a ela o valor 19.99. Em seguida, imprima o tipo da variável.
print('Questão 3')
preco = 19.99
print(type(19.99))
print("-------------------------------------------------------------------")

# Crie uma variável chamada `numero_inteiro` e atribua a ela um número inteiro de sua escolha. Imprima o tipo da variável.
print('Questão 4')
numero_inteiro = 5
print(type(numero_inteiro))
print("-------------------------------------------------------------------")

# Crie uma variável chamada `eh_estudante` e atribua a ela o valor booleano `True` ou `False`. Imprima o tipo da variável.
print('Questão 5')
eh_estudante = True
print(type(eh_estudante))
print("-------------------------------------------------------------------")


# Crie duas variáveis numéricas `a` e `b` e atribua a elas valores inteiros. Em seguida, calcule a soma,
# subtração, multiplicação e divisão dessas variáveis e imprima os resultados.
print('Questão 6')
a = 5
b = 2

print('Soma: ', a + b )
print('subtração: ', a - b )
print('multiplicação: ', a * b )
print('divisão: ', a / b )

print("-------------------------------------------------------------------")

# Crie duas variáveis de string `primeiro_nome` e `sobrenome`. Concatene-as para formar o nome completo e imprima o resultado.
print('Questão 7')

nome = "Eduardo"
sobrenome = "Freitas"
print(nome, sobrenome)
print("-------------------------------------------------------------------")

# Crie uma variável `idade_str` que armazena sua idade como uma string. Converta essa variável para um número inteiro e imprima o tipo da nova variável.
print('Questão 8')

idade_str = '25'
print(type(int(idade_str)))
print("-------------------------------------------------------------------")

# Crie uma variável `peso` com um valor decimal. Converta essa variável para uma string e imprima o resultado.
print('Questão 9')
peso = 90.2
peso_str = str(peso)
print(peso_str)
print("-------------------------------------------------------------------")

# Crie uma variável `frase` e atribua a ela uma frase de sua escolha. Imprima o tamanho da frase usando a função `len()`.
print('Questão 10')
frase = 'frase de sua escolha'
print(len(frase))

print("-------------------------------------------------------------------")

# Utilize a variável `frase` do exercício anterior e imprima a frase toda em maiúsculas.
print('Questão 11')
print(frase.upper())

print("-------------------------------------------------------------------")

# Divida a variável `frase` em uma lista de palavras usando o método `split()`. Em seguida, imprima a lista.
print('Questão 12')
print(frase.split())

print("-------------------------------------------------------------------")

# Peça ao usuário para digitar seu nome e idade. Armazene essas informações em variáveis e imprima uma mensagem personalizada utilizando essas variáveis.
print('Questão 13')
nome = input('Digite o seu nome ')
idade = input('Digite sua idade ')

print(f'Seu nome é nome: {nome}, e sua idade é: {idade}')

print("-------------------------------------------------------------------")