
class Pessoa:

    def __init__(self, nome: str, idade: int):

        self.nome = nome
        self.idade = idade

    def apresenta(self):

        print(f'Oi meu nome é {self.nome} e tenho {self.idade} anos.')

primeira_pessoa = Pessoa('Peter', 39)

print(primeira_pessoa.nome)
print(primeira_pessoa.idade)

class Brasileiro(Pessoa):

    def __init__(self, nome, idade, estado: str, cidade: str):
        super().__init__(nome, idade)
        self.estado = estado
        self.cidade = cidade

    def apresenta(self):
        super().apresenta()
        print(f'f Sou de {self.cidade} / {self.estado}.')

primeira_pessoa = Brasileiro('Peter', 39, 'São Paulo', 'São Bernardo')

print(primeira_pessoa.estado)
print(primeira_pessoa.cidade)