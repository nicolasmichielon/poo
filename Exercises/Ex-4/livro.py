from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__capitulos = []
        self.__autores = [autor]
        
        self.incluir_capitulo(numero_capitulo, titulo_capitulo)
            
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @property
    def autores(self):
        return self.__autores
        
    @property
    def capitulos(self):
        return self.__capitulos
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora


    def incluir_autor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor in self.__autores:
            self.__autores.remove(autor)


    def incluir_capitulo(self, numero: int, titulo: str):
        cap = Capitulo(numero, titulo)
        capExist = self.find_capitulo_by_titulo(titulo)
        if capExist is None:
            self.__capitulos.append(cap)

    def excluir_capitulo(self, titulo: str):
        for c in self.__capitulos:
            if c.titulo == titulo:
                self.__capitulos.remove(c)

    def find_capitulo_by_titulo(self, titulo: str):
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
        for c in self.__capitulos:
            if c.titulo == titulo:
                return c
        return None

