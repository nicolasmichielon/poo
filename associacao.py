class Professor():
    def __init__(self, nome, endereco, orientando):
        self.__nome = nome
        self.__endereco = endereco
        self.__orientando = orientando

    @property
    def orientando(self):
        return self.__orientando.nome
       


class Aluno():
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
    
    @property
    def nome(self):
        return self.__nome


nick2 = Aluno("Nicolas Michielon", "Florianopolis")
nick = Professor("Nicholas Derham", "Florianopolis", nick2)

print(nick.orientando)