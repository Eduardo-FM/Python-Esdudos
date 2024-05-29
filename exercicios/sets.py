"""
### Exercício 1
Crie um set com os números de 1 a 5 e outro set com os números de 4 a 8. Encontre a interseção entre esses dois sets.
"""

num1 = {1, 2, 3, 4, 5}
num2 = {4,5,6,7,8}
print(num1 & num2)
"""
### Exercício 2
Adicione o número 6 ao set `{1, 2, 3, 4, 5}`. Verifique se o número foi adicionado corretamente.
"""

num1.add(6)
print(num1)

"""
### Exercício 3
Remova o número 3 do set `{1, 2, 3, 4, 5}` e verifique se a remoção foi bem-sucedida.
"""

num1.remove(3)
print(num1)

"""
### Exercício 4
Dado o set `{1, 2, 3, 4, 5}`, verifique se o número 7 está presente no set.
"""
num = {1, 2, 3, 4, 5}

print(7 in num)

"""
### Exercício 5
Crie um set vazio e adicione os elementos "a", "b" e "c". Em seguida, remova todos os elementos desse set.
"""
vazio = set()
print(vazio)
vazio.update(['a', 'b', 'c'])
print(vazio)
vazio.clear()
print(vazio)
"""
### Exercício 6
Dados os sets `{1, 2, 3}` e `{4, 5, 6}`, encontre a união entre eles.
"""
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union = set1 | set2
print(union)  

"""
### Exercício 7
Crie um set com os elementos `{1, 2, 3, 4, 5}` e outro set com os elementos `{4, 5, 6, 7, 8}`. Encontre a diferença entre o primeiro e o segundo set.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 - set2)

"""
### Exercício 8
Verifique se o set `{1, 2, 3}` é um subconjunto do set `{1, 2, 3, 4, 5}`.
"""
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
"""
### Exercício 9
Dado o set `{10, 20, 30, 40, 50}`, encontre o maior e o menor elemento do set.
"""

set1 = {10, 20, 30, 40, 50}
print('Maior: ', max(set1))
print('Menor: ', min(set1))

"""
### Exercício 10
Remova todos os elementos do set `{1, 2, 3, 4, 5}` utilizando um único método.
"""
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)

"""
### Exercício 11
Dado o set `{1, 2, 3, 4, 5}`, crie uma cópia desse set.
"""
set1 = {1, 2, 3, 4, 5}
set2 = set1.copy()
print(set2)

"""
### Exercício 12
Crie um set com elementos repetidos da lista `[1, 2, 2, 3, 4, 4, 5]` e remova as duplicatas.
"""
list1 = [1, 2, 2, 3, 4, 4, 5]
set1 = set(list1)
print(set1)

"""
### Exercício 13
Verifique a diferença simétrica entre os sets `{1, 2, 3}` e `{3, 4, 5}`.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))

"""
### Exercício 14
Converta a lista `[1, 2, 3, 4, 5]` em um set e exiba o resultado.
"""

llista = [1, 2, 3, 4, 5]
set1 = set(llista)
print(set1)
"""
### Exercício 15
Dado o set `{1, 2, 3, 4, 5}`, use um loop para iterar sobre todos os elementos e imprimir cada um deles.
"""

set1 = {1, 2, 3, 4, 5}

for num in set1:
    print(num)