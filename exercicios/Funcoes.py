"""
1. Função de Saudação

Escreva uma função chamada saudar que receba um nome como argumento e retorne uma saudação no formato "Olá, [nome]!"
"""

def saudar(nome: str) -> str:
    return f"Olá {nome}, boa tarde!"

print(saudar('Eduardo'))

"""
2. Função de Soma

Crie uma função chamada soma que receba dois números e retorne a soma deles.
"""
def soma(num1: float, num2: float) -> float:
    try:
        return num1 + num2
    except TypeError as e:
        print(e)

print(soma(3, 5))
"""
3. Função de Fatorial

Escreva uma função chamada fatorial que calcule o fatorial de um número dado (um número inteiro não-negativo).
"""

def fatorial(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

print(fatorial(10))
"""
4. Função de Verificação de Primo

Crie uma função chamada é_primo que verifique se um número é primo.
"""
def eh_primo(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print(eh_primo(2))
"""
5. Função de Fibonacci

Escreva uma função chamada fibonacci que gere a sequência de Fibonacci até o n-ésimo termo.
"""

def fibonacci(n: int) -> int:
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(4))
"""
6. Função de Contagem de Vogais

Crie uma função chamada contar_vogais que conte o número de vogais em uma string fornecida.
"""

"""
7. Função de Inversão de String

Escreva uma função chamada inverter_string que retorne a string fornecida ao contrário.
"""

"""
8. Função de Máximo de Lista

Crie uma função chamada max_lista que receba uma lista de números e retorne o maior valor.
"""

"""
9 Uso de len()

Escreva um programa que use a função len() para contar o número de caracteres em uma string fornecida pelo usuário.
"""

"""
10. Uso de sum()

Crie um programa que use a função sum() para calcular a soma de todos os números em uma lista fornecida pelo usuário.
"""

"""
11. Uso de max() e min()

Escreva um programa que use as funções max() e min() para encontrar o maior e o menor número em uma lista de números fornecida pelo usuário.
"""

"""
12. Uso de sorted()

Crie um programa que use a função sorted() para ordenar uma lista de palavras fornecida pelo usuário em ordem alfabética.
"""

"""
13. Uso de map()

Escreva um programa que use a função map() para aplicar uma função que eleva ao quadrado cada número em uma lista de números fornecida pelo usuário.
"""

"""
14. Uso de filter()

Crie um programa que use a função filter() para filtrar todos os números ímpares de uma lista de números fornecida pelo usuário.
"""

"""
15. Uso de reduce()

Escreva um programa que use a função reduce() para calcular o produto de todos os números em uma lista fornecida pelo usuário 
(use from functools import reduce para importar reduce).
"""

"""
16. Uso de zip()

Crie um programa que use a função zip() para combinar duas listas de igual comprimento em uma lista de tuplas.
"""

"""
17. Verificação de Palíndromo

Escreva uma função chamada é_palíndromo que use a função inverter_string e 
outras funções embutidas para verificar se uma string é um palíndromo (lê-se da mesma forma de trás para frente).
"""

"""
18. Contagem de Frequência de Caracteres

Crie uma função chamada contar_frequencia que use um dicionário e funções embutidas para contar a frequência de cada caractere em uma string fornecida.
"""

"""
19. Conversão de Temperatura

Escreva uma função chamada celsius_para_fahrenheit e outra chamada fahrenheit_para_celsius que convertam temperaturas entre essas duas escalas. 
Use essas funções para criar um programa que converta uma lista de temperaturas fornecida pelo usuário.
"""

"""
20. Simulação de Lançamento de Dados

Crie uma função chamada lancar_dado que simule o lançamento de um dado (retorne um número aleatório entre 1 e 6). 
Use essa função para criar um programa que simule 1000 lançamentos e mostre a frequência de cada resultado.
"""