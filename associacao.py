class Aluno():
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
    
    @property
    def nome(self):
        return self.__nome


class Professor():
    def __init__(self, nome, endereco, orientando: Aluno):
        if(isinstance(orientando, Aluno)):
            self.__orientando = orientando
        else:
            self.__orientando = None
            print("Aluno incorreto.")
        self.__nome = nome
        self.__endereco = endereco

    @property
    def orientando(self):
        if(isinstance(self.__orientando, Aluno)):
            return self.__orientando.nome
        return False


nick2 = Aluno("Nicolas Michielon", "Florianopolis")
nick = Professor("Nicholas Derham", "Florianopolis", nick2)
nick3 = Professor("Nicholas Derham", "Florianopolis", nick)

print(nick.orientando)
print(nick3.orientando)