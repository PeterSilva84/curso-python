
class Animal:

    def __init__(self, raca: str, peso: int):

        self.raca = raca
        self.peso = peso

    # def apresenta(self):
    #
    #     print(f'A raça do animal é{self.raca} e o peso dele é {self.peso}')

class Cachorro(Animal):

    def __int__(self, raca, peso, nome: str, idade: int):
        super().__init__(raca, peso)
        self.nome = nome
        self.idade = idade

    def comer(self, alimento: str):
        print {f'o nome do cachorro é {self.nome}, e gosta de comer {alimento}'}

meu_cachorro = Cachorro('Vira lata', 20, 'Freud', 15)


#continua





