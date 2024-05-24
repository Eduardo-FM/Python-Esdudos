"""
Exercício 1: Divisão por Zero
Crie uma função chamada divide que receba dois números 
e retorne o resultado da divisão do primeiro pelo segundo. Trate a exceção de divisão por zero e retorne uma mensagem de erro apropriada.
"""


def divide(num1: int, num2: int) -> int:
    """
    A função recebe dois números e retorna o resultado da divisão do primeiro pelo segundo
    """ 
    try:
        divisao = num1/ num2
        return print(divisao)
    except ZeroDivisionError:
        print('não é possível realizar uma divisão por zero')


divide(10, 2)


"""
Exercício 2: Conversão de String para Inteiro
Escreva uma função convert_to_int que receba uma string e tente convertê-la para um inteiro. Se a conversão falhar, capture a exceção e retorne uma mensagem de erro.
"""

def conver_to_int(s: str) -> int:
    """
    Recebe uma String e tenta convertê-la para um inteiro.
    """
    try:
        return print(int(s))
    except ValueError: 
        print('Erro em converter essa string para um inteiro')

conver_to_int('a')

"""
Exercício 3: Acesso a Elementos em Listas
Crie uma função get_list_element que receba uma lista e um índice, e retorne o elemento na posição especificada. 
Se o índice estiver fora do intervalo da lista, capture a exceção e retorne uma mensagem de erro.

python
"""

def get_list_element(list: list, index: int) -> int:
    """
    Recebe uma lista e um índice, e retorna o elemento na posição especificada
    """
    try:
        return print(list[index])
    except IndexError: 
        print('Índice fora do intervalo da lista')
li = ['Laranja', 'Perâ', 'Maça'] 

get_list_element(li, 5)

"""
Exercício 4: Leitura de Arquivos
Escreva uma função read_file que tente abrir e ler o conteúdo de um arquivo. 
Capture exceções para lidar com casos onde o arquivo não existe ou não pode ser aberto, e retorne uma mensagem de erro.
"""

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except IOError:
        return f"Erro: Não foi possível ler o arquivo {file}."
    
print(read_file("exercicios\exemplo.txt"))


"""
Exercício 5: Custom Exception
Defina uma exceção personalizada NegativeValueError. 
Em seguida, escreva uma função check_positive que levante essa exceção se um valor negativo for passado. Capture a exceção e retorne uma mensagem de erro.
"""

class NegativeValueError(Exception):
    pass

def check_positive(value):
    try:
        if value < 0:
            raise NegativeValueError("Erro: Valor negativo fornecido.")
        return "Valor positivo."
    except NegativeValueError as e:
        return str(e)
    
print(check_positive(10))  
print(check_positive(-5)) 

"""
Exercício 6: Múltiplas Exceções
Escreva uma função process_input que receba um valor e tente converter para inteiro e depois dividir 100 por esse valor. 
Trate tanto a conversão inválida quanto a divisão por zero com mensagens apropriadas.
"""

def process_input(s: str) -> float:
    try:
        num = int(s)
        divisao = 100 / num
        print(divisao)
        return divisao
    except ValueError:
        print('Erro em converter essa string para um inteiro')
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por zero') 

process_input('0')

"""
Exercício 7: Finally
Crie uma função open_file que sempre feche o arquivo após a leitura, independentemente de exceções. 
Use um bloco finally para garantir que o arquivo seja fechado.
"""

def open_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        return file.read()
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except IOError:
        return "Erro: Não foi possível ler o arquivo."
    finally:
        if file:
            file.close()

print(open_file("exercicios\exemplo.txt")) 