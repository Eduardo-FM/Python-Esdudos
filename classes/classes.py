class Pessoa:
    def __init__(self, nome: str, idade: int, estudante: bool) -> object:
        self.nome = nome
        self.idade = idade
        self.estudante = estudante

    def __str__(self) -> str:
        return f'Pessoa: {self.nome}, idade: {self.idade}, estudante: {self.estudante}'
    
    def listar_linguagens(self, *lingaguens: str):
        print(f'Olá, meu nome é {self.nome}, e estou estudando as linguagens de programação: {lingaguens}')

    

pessoa = Pessoa('Eduardo', 25, True)
pessoa.idade = 30
print(pessoa)
pessoa.profissao = 'programador'

print(pessoa.profissao)


#pessoa.listar_linguagens('Java', 'Python')