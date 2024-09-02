class Aluno():
    def __init__(self, nome: str, idade: int, mat: int):
        if (isinstance(idade, str)):
            self.__nome = nome
            self.__idade = idade
            self.__mat = mat
        else:
            print("instanciação incorreta")
            exit()
        
    def mostra_dados(self):
        print("\n\nDados do aluno: ")
        print("Nome: ", self.__nome)
        print("Idade: ", self.__idade)
        print("Matrícula: ", self.__mat)
        print("\n")
    
    def faz_aniversario(self):
        self.__idade += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def mat(self):
        return self.__mat

    @nome.setter
    def nome(self, nome):
        if (type(nome) == str):
            self.__nome = nome
        else:
            print("Name is not a string")

    @mat.setter
    def mat(self, mat):
        if (type(mat) == int):
            self.__mat = mat
        else:
            print("Matrícula is not an integer")

    
    

n1 = Aluno("Mestre", 20, 12345678)
n2 = Aluno("Nícolas", 20, 23456789)
a1 = Aluno("Arthur", 16, 45678910)
p1 = Aluno("Pedro", "18", 13579246)

n1.nome = "Nicholas"
n2.mat = "matricula muito longa"

n1.faz_aniversario()
print(n1.mostra_dados())
p1.faz_aniversario()

print(n1.nome)
print(n2.nome)
print(p1.nome)

print(n2.idade)
print(a1.idade)

print(n1.mat)
print(n2.mat)
print(a1.mat)



