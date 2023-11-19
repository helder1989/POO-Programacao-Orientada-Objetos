# metodos @property - Getters e Setters
# Getters: obtem um valor e o Setters configura um valor

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getters, sempre que pedir um valor esse metodo será chamado primeiro
    @property
    def preco(self):
        return self._preco

    # Setters, sempre que for atrivuir um valor esse metodo será chamado primeiro e depois vai configurar o preco
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor




p1 = Produto('Creatina', 'R$20')
p1.desconto(20)
print(p1.preco)

p2 = Produto('Camiseta', 70)
p2.desconto(40)
print(p2.preco)

