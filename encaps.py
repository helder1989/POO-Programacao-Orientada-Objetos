# Encapsulamento

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property # me concede acesso à variavel __dados
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome}) #  atualizando o dicionário

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def delet_cliente(self, id):
        del self.__dados['clientes'] [id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Helder')
bd.inserir_cliente(2, 'Mirandinha')
bd.inserir_cliente(3, 'Kevin')
bd.lista_clientes()
print(bd.dados)




