

class Singleton:

    __intance = None

    def __init__(self) -> None:
        if not Singleton.__intance:
            print('O metodo __init__ foi chamado...')
        else:
            print(f"A instancia ja foi criada: {self.get_instance()}")
    
    @classmethod
    def get_instance(cls):
        if not cls.__intance:
            cls.__intance = Singleton()
        return cls.__intance



s1 = Singleton() # A classe é inicializada mas o objeto nao é criado..
print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton() # Instancia ja criada
