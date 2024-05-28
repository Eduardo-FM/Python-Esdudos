"""
1. Criação e Acesso a Elementos:

- Crie uma lista com 5 números inteiros.
- Acesse e imprima o primeiro e o último elemento da lista.
"""

llist = [1, 2, 3, 4, 5]

print('Primeiro núemro =', llist[0],  '. Último número', llist[-1])

"""
2. Adição de Elementos:

- Adicione o número 10 ao final da lista.
- Adicione o número 0 no início da lista
"""

llist.append(10)

print(llist)

llist.insert(0, 0)
print(llist)

"""
3. Remoção de Elementos:

- Remova o primeiro elemento da lista.
- Remova o último elemento da lista.
- Remova o número 10 da lista (use a função remove).
"""
llist.pop(0)
print(llist)

llist.pop()
print(llist)

llist.remove(5)
print(llist)

"""
## 4. Iteração sobre a Lista
- Use um loop `for` para imprimir todos os elementos da lista.
- Use um loop `while` para imprimir todos os elementos da lista.
"""

for num in llist:
    print(num)

i = 0
while i < llist.__len__():
    print(llist[i])
    i += 1

"""
## 5. List Comprehension
- Crie uma nova lista que contém o quadrado de cada número da lista original.

"""

lista_quadrado = [num ** 2 for num in llist]
print(lista_quadrado)

"""
## 6. Operações com Listas
- Some todos os elementos da lista.
- Encontre o maior e o menor número da lista.

"""

print('Soma:', sum(lista_quadrado))
print('Maior:', max(lista_quadrado))
print('Menor:', min(lista_quadrado))

"""
## 7. Filtragem de Listas
- Crie uma nova lista que contenha apenas os números pares da lista original.
- Crie uma nova lista que contenha apenas os números maiores que 5 da lista original.

"""

pares = [x for x in llist if x % 2 == 0]
print(pares)

impares = [x for x in llist if x % 2 != 0]
print(impares)

"""
## 8. Ordenação de Listas
- Ordene a lista em ordem crescente.
- Ordene a lista em ordem decrescente.

"""
llist = [3, 2, 1, 4, 5]
print(llist)

crescente = sorted(llist)

print('Lista crescente: ',crescente)

decrescente = sorted(llist, reverse = True)

print('Lista decrescente: ', decrescente)

"""
## 9. Combinando Listas
- Crie uma segunda lista com 5 números inteiros diferentes.
- Combine as duas listas em uma só.

"""

nova_lista = [6,7,8,9,10]


llist = llist + nova_lista
print(llist)


"""
## 10. Operações Avançadas
- Crie uma lista de listas (matriz) de tamanho 3x3.
- Acesse e imprima um elemento específico dessa matriz (por exemplo, o elemento na posição [1][2]).
- Calcule a soma de todos os elementos da matriz.
"""

matriz = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]

print(matriz[1][2])

print('-----------------------------------------------------')
print(sum(sum(linha) for linha in matriz))
"""
## 11. Funções com Listas
- Escreva uma função que receba uma lista e retorne a soma dos seus elementos.
- Escreva uma função que receba uma lista e retorne uma nova lista com os elementos em ordem inversa.

"""

def soma_lista(llista: list) -> int:
    return sum(llista)

def lista_inversa(llista: list) -> list:
    return sorted(llista, reverse = True)

print(llist)
print('Soma: ', soma_lista(llist))
print('Inversa: ', lista_inversa(llist))

"""
## 12. Métodos de Lista
- Use o método `count` para contar quantas vezes um determinado número aparece na lista.
- Use o método `index` para encontrar a posição de um determinado número na lista.

"""
llist = [1,2,3,4,5,2,3,2,1]

print(llist.count(2))

print(llist.index(3))

"""
## 13. Fatiamento de Listas
- Crie uma sublista contendo apenas os 3 primeiros elementos da lista original.
- Crie uma sublista contendo apenas os 3 últimos elementos da lista original.
- Crie uma sublista contendo os elementos do índice 1 ao 4.

"""

nova_lista = llist[0:3]
print(nova_lista)
nova_lista = llist[-1: -4]
print(llist[-3])
nova_lista = llist[1:5]
print(nova_lista)

"""
## 14. Manipulação de Strings em Listas
- Crie uma lista de strings.
- Concatene todas as strings em uma única string.
- Crie uma nova lista contendo o comprimento de cada string na lista original.

"""
lista_string = ['ba', 'ca','da','fa']
print(''.join(lista_string))

print([len(s) for s in lista_string])

"""
## 15. Desafios Extras
- Escreva uma função que receba uma lista de números e retorne uma lista contendo apenas os números primos.
- Escreva uma função que receba uma lista de strings e retorne uma lista de strings que são palíndromos.
"""

def num_primos(list: list) -> list:
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [x for x in list if eh_primo(x)]

def palindromos(lst):
    return [s for s in lst if s == s[::-1]]

print(num_primos([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: [2, 3, 5, 7]
print(palindromos(["ana", "python", "radar", "solos"]))    # Output: ["ana", "radar", "solos"]