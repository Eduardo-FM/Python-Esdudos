"""
1. **Criação de Dicionário**
   - Crie um dicionário que mapeie nomes de estudantes às suas respectivas notas.
   - Exemplo: `{"Alice": 8.5, "Bob": 7.0, "Charlie": 9.0}`.
"""
nomes_estudantes = {"Alice": 8.5, "Bob": 7.0, "Charlie": 9.0}
"""
2. **Acesso a Valores**
   - Dado um dicionário com preços de frutas, acesse o preço da maçã.
   - Exemplo: `{"maçã": 2.5, "banana": 1.0, "laranja": 3.0}`.
"""
frutas = {"maçã": 2.5, "banana": 1.0, "laranja": 3.0}
print(frutas['maçã'])
"""
3. **Adicionar Itens**
   - Adicione um novo item ao dicionário criado no exercício 1: um estudante chamado "David" com nota 6.5.
"""
nomes_estudantes['David'] = 6.5
print(nomes_estudantes)
"""
4. **Remover Itens**
   - Remova o item com a chave "Bob" do dicionário criado no exercício 1.
"""
nomes_estudantes.pop('Bob')
print(nomes_estudantes)
"""
5. **Iteração sobre Dicionários**
   - Itere sobre o dicionário criado no exercício 1 e imprima cada nome de estudante e sua respectiva nota.
"""
nomes_estudantes = {"Alice": 8.5, "Bob": 7.0, "Charlie": 9.0}

for estudante, nota in nomes_estudantes.items():
    print(f'{estudante}: {nota}')
"""
6. **Verificação de Chaves**
   - Verifique se o nome "Eve" está presente no dicionário criado no exercício 1.
"""

print('Eve' in nomes_estudantes)
"""
7. **Dicionário Aninhado**
   - Crie um dicionário aninhado que mapeie cada estudante para outro dicionário contendo suas notas em diferentes matérias.
   - Exemplo: `{"Alice": {"matemática": 8.5, "história": 9.0}, "Bob": {"matemática": 7.0, "história": 6.5}}`.
"""
dicionario_aninhado = {"Alice": {"matemática": 8.5, "história": 9.0}, "Bob": {"matemática": 7.0, "história": 6.5}}
print(dicionario_aninhado)
"""
8. **Combinação de Dicionários**
   - Combine dois dicionários em um só. Exemplo: `{"a": 1, "b": 2}` e `{"c": 3, "d": 4}`.
"""
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
combined_dict = {**dic1, **dic2}
print(combined_dict)
"""
9. **Comprimento do Dicionário**
   - Escreva um programa que encontre o número de pares chave-valor no dicionário criado no exercício 1.
"""
nomes_estudantes = {"Alice": 8.5, "Bob": 7.0, "Charlie": 9.0}
print(len(nomes_estudantes))
"""
10. **Valor Máximo**
    - Encontre o estudante com a nota mais alta no dicionário criado no exercício 1.
"""
print(max(nomes_estudantes, key=nomes_estudantes.get))
"""
11. **Atualizar Valor**
    - Atualize a nota do estudante "Charlie" para 9.5 no dicionário criado no exercício 1.
"""
nomes_estudantes['Charlie'] = 9.5
print(nomes_estudantes)
"""
12. **Conversão de Listas em Dicionário**
    - Dadas duas listas: uma com nomes de estudantes e outra com suas respectivas notas, converta-as em um dicionário.
    - Exemplo: `["Alice", "Bob", "Charlie"]` e `[8.5, 7.0, 9.0]`.
"""
lista1 = ["Alice", "Bob", "Charlie"]
lista2 = [8.5, 7.0, 9.0]
novo_dic = dict(zip(lista1, lista2))
print(novo_dic)
"""
13. **Dicionário Invertido**
    - Inverta as chaves e valores do dicionário criado no exercício 1. Exemplo: `{8.5: "Alice", 7.0: "Bob", 9.0: "Charlie"}`.
"""
notas_estudantes_invertido = {nota: estudante for estudante, nota in nomes_estudantes.items()}
print(notas_estudantes_invertido)

"""
14. **Filtro em Dicionário**
    - Filtre os estudantes com notas maiores que 8.0 do dicionário criado no exercício 1.
"""
print({estudante: nota for estudante, nota in nomes_estudantes.items() if nota > 8 })
"""
15. **Contagem de Frequência**
    - Dada uma lista de palavras, conte a frequência de cada palavra usando um dicionário.
    - Exemplo: `["apple", "banana", "apple", "orange", "banana", "apple"]`.
"""

lista_frutas = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequencia_palavras = {}
for palavra in lista_frutas:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

print(frequencia_palavras)