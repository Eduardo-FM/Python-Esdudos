"""
### Exercício 1: Soma de Dois Números
Escreva uma função lambda que receba dois números e retorne a soma deles.
"""
soma  = lambda x,y: x + y
"""
### Exercício 2: Verificação de Paridade
Crie uma função lambda que receba um número e retorne `True` se ele for par e `False` caso contrário.
"""
paridade = lambda x: x % 2 == 0
"""
### Exercício 3: Comprimento da String
Desenvolva uma função lambda que receba uma string e retorne o comprimento dessa string.
"""
comprimento = lambda string: len(string)
"""
### Exercício 4: Potência de um Número
Escreva uma função lambda que receba dois números, `base` e `expoente`, e retorne o resultado de `base` elevado à `expoente`.
"""

potencia = lambda base, expoente: base ** expoente 

"""
### Exercício 5: Filtrando Números Pares
Use uma função lambda dentro de uma função `filter` para obter apenas os números pares de uma lista de números.
"""

lista = [1,2,3,4,5,6]
numeros_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

"""
### Exercício 6: Quadrado dos Números
Utilize uma função lambda dentro de uma função `map` para obter o quadrado de todos os números de uma lista.
"""
lista = [1,2,3,4,5,6]

quadrados = lambda lista: list(map(lambda x: x ** 2, lista))

print(quadrados(lista))


"""
### Exercício 7: Ordenação por Segunda Letra
Crie uma função lambda para ordenar uma lista de palavras pela segunda letra de cada palavra.
"""
palavras = ['ab', 'ba', 'cd', 'ac' ]

ordenar_por_segunda_letra = lambda palavras: sorted(palavras, key=lambda x: x[1])

print(ordenar_por_segunda_letra(palavras))


"""
### Exercício 8: Contar Letras A
Escreva uma função lambda que conte quantas vezes a letra 'a' aparece em uma string.
"""
contar_str: str = lambda contador: contador.count('a')

print(contar_str('abacati'))

"""
### Exercício 9: Verificação de Palíndromo
Desenvolva uma função lambda que verifique se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).
"""

palindromo: str = lambda string: string == string[::-1]
print(palindromo('aba'))

"""
### Exercício 10: Filtrando Palavras Longas
Use uma função lambda dentro de uma função `filter` para obter apenas as palavras com mais de 5 caracteres de uma lista de palavras.
"""
palavras = ['baka', 'flamengo', 'cu', 'pintos']

palavras_longas = lambda palavras: list(filter(lambda string: len(string) > 5, palavras))

print(palavras_longas(palavras))

"""
### Exercício 11: Somatório de uma Lista
Escreva uma função lambda que receba uma lista de números e retorne o somatório de todos os elementos.
"""
lista = [1,2,3,4,5,6]

somatorio = lambda somatorio: sum(somatorio)

print(somatorio(lista))
"""
### Exercício 12: Multiplicação por Constante
Crie uma função lambda que receba um número e retorne o resultado de sua multiplicação por uma constante `k`.
"""
multiplicar_por_k = lambda x, k: x * k
print(multiplicar_por_k(2,5))
"""
### Exercício 13: Filtrando Strings que Começam com uma Letra
Use uma função lambda dentro de uma função `filter` para obter apenas as strings que começam com uma letra específica de uma lista de strings.
"""
palavras = ['baka', 'flamengo', 'bacu', 'pintos']

comeca_com_letra = lambda palavras, letra: list(filter(lambda x: x.startswith(letra), palavras))

print(comeca_com_letra(palavras, 'b'))
"""
### Exercício 14: Remover Espaços em Branco
Escreva uma função lambda que receba uma string e retorne a string sem espaços em branco.
"""

remove_espacos = lambda string : string.lower().replace(' ', '')

print(remove_espacos('g3x sera campea'))

"""
### Exercício 15: Verificação de Maiúsculas
Crie uma função lambda que receba uma string e retorne `True` se todos os caracteres forem maiúsculos e `False` caso contrário.
"""

verifica_maiscula = lambda string: string.isupper()
print(verifica_maiscula('G3X'))

"""
### Exercício 16: Concatenação de Strings
Desenvolva uma função lambda que receba duas strings e retorne a concatenação delas.
"""

concatenacao_strings = lambda str1, str2: str1 + str2
print(concatenacao_strings('g3x', 'campea'))

"""
### Exercício 17: Multiplicação de Dois Números
Escreva uma função lambda que receba dois números e retorne o produto deles.
"""

multiplicacao = lambda num1, num2 : num1 * num2
print(multiplicacao(2,5))

"""
### Exercício 18: Comparação de Comprimentos
Crie uma função lambda que compare o comprimento de duas strings e retorne `True` se forem iguais e `False` caso contrário.
"""

comparacao_comprimentos = lambda str1, str2 : len(str1) == len(str2)

print(comparacao_comprimentos('g3x', 'abc'))
"""
### Exercício 19: Filtrando Números Negativos
Use uma função lambda dentro de uma função `filter` para obter apenas os números negativos de uma lista de números.
"""
numeros_negativos = lambda lista: list(filter(lambda x: x < 0, lista))
"""
### Exercício 20: Transformação de Lista
Utilize uma função lambda dentro de uma função `map` para adicionar 10 a cada elemento de uma lista de números.
"""
lista = [1,2,3,4,5,6]

transformar_lista = lambda lista: list(map(lambda num: num + 10, lista))

print(transformar_lista(lista))