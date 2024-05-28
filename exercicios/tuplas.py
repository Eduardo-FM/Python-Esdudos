"""
## Exercício 1: Criação de Tuplas
Crie uma tupla chamada `minha_tupla` contendo os seguintes elementos: 1, 2, 3, 'a', 'b', 'c'. Imprima a tupla.
"""
minha_tupla = ( 1, 2, 3, 'a', 'b', 'c')
print(minha_tupla)

"""
## Exercício 2: Acesso a Elementos da Tupla
Dada a tupla `minha_tupla = (10, 20, 30, 40, 50)`, imprima o primeiro e o último elemento.
"""
minha_tupla = (10, 20, 30, 40, 50)
print(minha_tupla[0])
print(minha_tupla[-1])
"""
## Exercício 3: Concatenando Tuplas
Crie duas tuplas `tupla1` e `tupla2`. Concatene as duas tuplas e imprima o resultado.
"""
tupla1 = ( 1, 2, 3, 'a', 'b', 'c')
tupla2 = (10, 20, 30, 40, 50)

print(tupla1 + tupla2)
print('-----------------------------------------------------------------')

"""
## Exercício 4: Fatiamento de Tuplas
Dada a tupla `tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)`, imprima uma sub-tupla contendo os elementos do índice 2 ao índice 5.
"""
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla[2:6])

"""
## Exercício 5: Verificar Existência de Elemento
Verifique se o elemento 5 está na tupla `minha_tupla = (1, 2, 3, 4, 5)`.
"""
minha_tupla = (1, 2, 3, 4, 5)
print(5 in minha_tupla)

"""
## Exercício 6: Contar Ocorrências de um Elemento
Dada a tupla `tupla = (1, 2, 2, 3, 4, 4, 4, 5)`, conte quantas vezes o número 4 aparece na tupla.
"""

print(minha_tupla.count(4))
"""
## Exercício 7: Encontrar Índice de um Elemento
Encontre o índice da primeira ocorrência do número 3 na tupla `tupla = (1, 2, 3, 4, 3, 2, 1)`.
"""

print(minha_tupla.index(3))
"""
## Exercício 8: Desempacotamento de Tuplas
Dada a tupla `tupla = ('a', 'b', 'c')`, desempacote seus elementos em três variáveis `x`, `y` e `z` e imprima-as.
"""
tupla = ('a', 'b', 'c')
x, y, z = tupla
print(x)
print(y)
print(z)
"""
## Exercício 9: Tupla de Tuplas
Crie uma tupla de tuplas chamada `tupla_de_tuplas` contendo as seguintes tuplas: (1, 2), (3, 4), (5, 6). Acesse e imprima o segundo elemento da segunda tupla.
"""
tupla_de_tuplas = (1, 2), (3, 4), (5, 6)
print(tupla_de_tuplas[1][1])

"""
## Exercício 10: Conversão de Lista para Tupla
Converta a lista `lista = [1, 2, 3, 4, 5]` em uma tupla e imprima-a.
"""
lista = [1, 2, 3, 4, 5]
x = tuple(lista)
print(x)


"""
## Exercício 11: Imutabilidade de Tuplas
Tente alterar o primeiro elemento da tupla `tupla = (1, 2, 3)` para o valor 10 e observe o que acontece.
"""
#tupla = (1, 2, 3)
#tupla[0] = 10
#print(tupla[0])
"""
## Exercício 12: Tamanho da Tupla
Calcule e imprima o tamanho da tupla `tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`.
"""
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tupla))

"""
## Exercício 13: Uso de Funções com Tuplas
Dada a tupla `tupla = (5, 3, 8, 1, 9)`, use as funções `min` e `max` para encontrar e imprimir o menor e o maior elemento.
"""
tupla = (5, 3, 8, 1, 9)
print('Maior valor: ', max(tupla))
print('Menor valor: ', min(tupla))