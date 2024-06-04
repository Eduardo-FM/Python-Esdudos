"""
## Exercício 1: Criando um Iterator Básico
Crie um iterator que percorra os números de 1 a 10. Use a classe `Iterator` e implemente os métodos `__iter__()` e `__next__()`.
"""
class Numbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

num_iterator = Numbers(1, 10)
for num in num_iterator:
    print(num)

"""
## Exercício 2: Iterator de String
Crie um iterator que percorra cada caractere de uma string fornecida. O iterator deve retornar os caracteres um por um.
"""

class StringIterator:
    def __init__(self, string) -> None:
        self.string = string
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        else:
            char = self.string[self.index]
            self.index += 1
            return char
        
str_iterator = StringIterator('Eduardo')
for char in str_iterator:
    print(char)

"""
## Exercício 3: Iterator Personalizado
Crie um iterator que percorra uma lista de números e retorne apenas os números pares.
"""

class EvenNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration
            
even_iterator = EvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for num in even_iterator:
    print(num)

"""
## Exercício 4: Iterador Infinito
Crie um iterator infinito que gere a sequência de números naturais (0, 1, 2, 3, ...). Implemente um método que permita interromper a iteração após 100 números.
"""
class InfiniteIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current - 1

infinite_iterator = InfiniteIterator()
for i in range(100):
    print(next(infinite_iterator))


"""
## Exercício 5: Iterador Reverso
Crie um iterator que percorra uma lista de elementos na ordem inversa.
"""
class InverseIterator:
    def __init__(self, items):
        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            item = self.items[self.index]
            self.index -= 1
            return item

inverser_iterator = InverseIterator([1,2,3,4,5])
for num in inverser_iterator:
    print(num)

"""
## Exercício 6: Contador com Limite
Crie um iterator que se comporte como um contador, começando de um valor inicial e incrementando até um valor final. O iterator deve ter um passo de incremento configurável.
"""
class Counter:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            current_value = self.current
            self.current += self.step
            return current_value

counter = Counter(1, 10, 2)
for num in counter:
    print(num)

"""
## Exercício 7: Filtro de Iteração
Implemente um iterator que recebe outro iterator como entrada e filtre os elementos com base em uma condição fornecida. 
Por exemplo, retornar apenas os elementos que são maiores que 5.
"""
class FilterIterator:
    def __init__(self, iterator, condition):
        self.iterator = iterator
        self.condition = condition

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.iterator)
            if self.condition(item):
                return item

def greater_than_five(x):
    return x > 5

numbers = iter([1, 2, 3, 6, 7, 8])
filtered_iterator = FilterIterator(numbers, greater_than_five)
for num in filtered_iterator:
    print(num)


"""
## Exercício 8: Iterando sobre Dicionários
Crie um iterator que percorra as chaves de um dicionário. Em seguida, modifique-o para percorrer os valores e, finalmente, para percorrer os itens (chave, valor).
"""
class DictKeysIterator:
    def __init__(self, d):
        self.d = d
        self.keys = list(d.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        else:
            key = self.keys[self.index]
            self.index += 1
            return key

d = {'a': 1, 'b': 2, 'c': 3}
keys_iterator = DictKeysIterator(d)
for key in keys_iterator:
    print(key)

class DictValuesIterator:
    def __init__(self, d):
        self.d = d
        self.values = list(d.values())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        else:
            value = self.values[self.index]
            self.index += 1
            return value

values_iterator = DictValuesIterator(d)
for value in values_iterator:
    print(value)

class DictItemsIterator:
    def __init__(self, d):
        self.d = d
        self.items = list(d.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        else:
            item = self.items[self.index]
            self.index += 1
            return item

items_iterator = DictItemsIterator(d)
for item in items_iterator:
    print(item)
"""
## Exercício 9: Iterando em um Arquivo
Crie um iterator que percorra cada linha de um arquivo de texto e retorne uma linha por vez.
"""
class FileIterator:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

file_iterator = FileIterator('example.txt')
for line in file_iterator:
    print(line)
"""
## Exercício 10: Combinando Iteradores
Crie um iterator que combine dois iteradores diferentes, alternando os elementos de cada um.
"""
class CombinedIterator:
    def __init__(self, iterator1, iterator2):
        self.iterator1 = iterator1
        self.iterator2 = iterator2
        self.use_first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.use_first:
            try:
                return next(self.iterator1)
            except StopIteration:
                self.use_first = False
        return next(self.iterator2)

iterator1 = iter([1, 3, 5])
iterator2 = iter([2, 4, 6])
combined_iterator = CombinedIterator(iterator1, iterator2)
for item in combined_iterator:
    print(item)
