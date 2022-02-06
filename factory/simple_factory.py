from abc import abstractmethod, ABCMeta

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print("Au Au")

class Gato(Animal):

    def falar(self):
        print("Miau")

class Camelo(Animal):

    def falar(self):
        print("Ta quente!")



# Fábrica

class Fabrica:
# eval é uma funcao que tenta transformar o valor recebido em um codigo python
    def criar_animal_falante(self, tipo):
        return eval(tipo)().falar()

# Cliente
if __name__ == '__main__':
    fab = Fabrica()
    animal = input("Qual animal vc quer que fale? [Cachorro, Gato e Camelo]").title()
    fab.criar_animal_falante(animal)