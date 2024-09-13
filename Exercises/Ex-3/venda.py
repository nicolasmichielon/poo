class Venda():
    def __init__(self, codigo, cliente, descricao, pacote, quantidade):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = pacote
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pacote(self):
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote):
        self.__pacote = pacote

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def preco_total(self):
        preco_total = self.__pacote.custo_unitario * self.__quantidade
        return preco_total