

class SanidadeCheck:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck,cls).__new__(cls,*args, **kwargs)
        return SanidadeCheck.__instance

    def __init__(self) -> None:
        self.__servidores = []

    def checar_servidores(self, srv):
        print(f"Checando p {self.__servidores[srv]}")

    def add_servidor(self):
        self.__servidores.append('Servidor1')
        self.__servidores.append('Servidor2')
        self.__servidores.append('Servidor3')
        self.__servidores.append('Servidor4')

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor5')


sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print(f'Cronograma de checagem de sanidade dos servidores A...')
for srv in range(4):
    sc1.checar_servidores(srv)

sc2.mudar_servidor()
print(f'Cronograma de checagem de sanidade dos servidores B...')
for srv in range(4):
    sc2.checar_servidores(srv)