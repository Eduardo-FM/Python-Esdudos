"""
## Exercício 1: Classe Pessoa
Crie uma classe chamada `Pessoa` que possua os atributos `nome`, `idade` e `email`. Adicione métodos para definir e obter esses atributos.
"""
class Pessoa:
    def __init__(self, nome, idade, email) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade
    
    def set_email(self, email):
        self.email = email
    
    def get_email(self):
        return self.email
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.idade} - {self.email}'
    

"""
## Exercício 2: Classe Carro
Implemente uma classe `Carro` com os atributos `marca`, `modelo` e `ano`. Crie um método que exibe as informações do carro e um método que calcula a idade do carro.
"""

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self) -> str:
        return f'Carro da marca: {self.marca}, modelo: {self.modelo}, ano de fabricação: {self.ano}'
    
    
    def calcula_idade_carro(self, ano_atual):
        return ano_atual - self.ano

"""
## Exercício 3: Classe Conta Bancária
Crie uma classe `ContaBancaria` com os atributos `numero_conta`, `titular` e `saldo`. Adicione métodos para depositar, sacar e consultar o saldo da conta.
"""

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo) -> None:
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def consultar(self):
        return f'Saldo da conta bancária: {self.saldo}'
"""
## Exercício 4: Classe Retângulo
Implemente uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos para calcular a área e o perímetro do retângulo.
"""

class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

"""
## Exercício 5: Classe Funcionário
Crie uma classe `Funcionario` com os atributos `nome`, `salario` e `cargo`. Adicione um método para aumentar o salário em uma determinada porcentagem.
"""

class Funcionario:

    taxa_de_aumento = 1.04

    def __init__(self, nome, salario, cargo) -> None:
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

"""
## Exercício 6: Herança - Classe Animal
Crie uma classe base chamada `Animal` com um método `falar`. Implemente duas subclasses, `Cachorro` e `Gato`, que herdam de `Animal` e sobrescrevem o método `falar`.
"""

class Animal:
    def __init__(self) -> None:
        pass

    def falar(self, som):
        return f'{som}'

class Cachorro(Animal):
    
    
    def falar(self):
        return print('AUAU')

class Gato(Animal):

    def falar(self, ):
        return print('MIAU')
"""
## Exercício 7: Classe Pilha
Implemente uma classe `Pilha` que simula o funcionamento de uma pilha (estrutura de dados LIFO). A classe deve ter métodos para empilhar, 
desempilhar e verificar se a pilha está vazia.
"""
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0
"""
## Exercício 8: Classe Fila
Crie uma classe `Fila` que simula o funcionamento de uma fila (estrutura de dados FIFO). 
A classe deve ter métodos para enfileirar, desenfileirar e verificar se a fila está vazia.
"""
class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def esta_vazia(self):
        return len(self.itens) == 0
"""
## Exercício 9: Classe Livro
Implemente uma classe `Livro` com os atributos `titulo`, `autor` e `ano_publicacao`. 
Adicione um método que exibe as informações do livro e um método que verifica se o livro é antigo (publicado há mais de 20 anos).
"""

class Livro:
    def __init__(self, titulo, autor,ano_publicacao) -> None:
        self.titulo = titulo 
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self) -> str:
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}'
    
    def livro_eh_antigo(self, ano_atual):
        if ano_atual - self.ano_publicacao >= 20:
            return f'O livro {self.titulo} é antigo'
        return f'O libro {self.titulo} é novo'
"""
## Exercício 10: Polimorfismo - Classe Forma
Crie uma classe base chamada `Forma` com um método `area`. 
Implemente duas subclasses, `Circulo` e `Quadrado`, que herdam de `Forma` e implementam o método `area` de acordo com suas fórmulas específicas.
"""
class Forma:

    def area(self) -> int:
        pass

class Circulo(Forma):
    
    _PI = 3.14

    def area(self, raio_do_circulo) -> int:
        return self._PI * (raio_do_circulo ** 2)
    
class Quadrado(Forma):
    
    def area(self, largura) -> int:
        return largura ** 2

"""
## Exercício 11: Classe Agenda
Implemente uma classe `Agenda` que permita adicionar, remover e listar contatos. 
Cada contato deve ser representado por um objeto da classe `Contato`, que possui os atributos `nome` e `telefone`.
"""
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:

    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome != nome]

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")

"""
## Exercício 12: Classe Empresa
Crie uma classe `Empresa` com os atributos `nome`, `cnpj` e uma lista de funcionários. 
Adicione métodos para contratar e demitir funcionários, bem como um método para listar todos os funcionários.
"""

class Funcionario():
    
    def __init__(self, nome, telefone) -> None:
        self.nome = nome
        self.telefone = telefone

class Empresa():
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def demitir_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'Nome: {funcionario.nome}, Telefone: {funcionario.telefone}')
"""
## Exercício 13: Classe Veículo e subclasses
Implemente uma classe base `Veiculo` com os atributos `marca` e `modelo`. 
Crie duas subclasses, `Carro` e `Moto`, que herdam de `Veiculo` e adicionam atributos específicos como `num_portas` para carros e `cilindradas` para motos.
"""

class Veiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas) -> None:
        super().__init__(marca, modelo)
        self.num_portas = num_portas

class Motos(Veiculo):
    def __init__(self, marca, modelo, cilindradas) -> None:
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
"""
## Exercício 14: Classe Produto
Crie uma classe `Produto` com os atributos `nome`, `preco` e `quantidade_em_estoque`. 
Adicione métodos para ajustar o preço e a quantidade em estoque, além de um método para exibir as informações do produto.
"""
class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
        
    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco

    def ajustar_quantidade(self, quantidade):
        self.quantidade_em_estoque = quantidade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Preço: {self.preco}, Quantidade em estoque: {self.quantidade_em_estoque}")
"""
## Exercício 15: Classe Jogo
Implemente uma classe `Jogo` com os atributos `titulo`, `desenvolvedor` e `genero`. 
Adicione métodos para exibir as informações do jogo e verificar se o jogo é de um determinado gênero.
"""

class Jogo:
    def __init__(self, titulo, desenvolvedor, genero) -> None:
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.genero = genero
    
    def exibir(self):
        print(f'Desenvolvedor: {self.desenvolvedor}, Titulo: {self.titulo}, Género: {self.genero}')

    def verifica_genero(self, genero):
        return self.genero.lower() == genero.lower