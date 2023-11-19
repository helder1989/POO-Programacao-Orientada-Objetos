from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # esse é um metodo normal, metodo de uma instancia, precisa da instancia em si
        print(self.ano_atual - self.idade)

    @classmethod  # criando um método da class. Nesse caso não preciso de uma instancia, mas preciso da classe em si
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)  # abre e fecha () pois estou chamando a class

    @staticmethod  # Não precisa nem da instancia e nem da class
    def gera_id():
        rand = randint(1000, 19999)
        return rand


# p1 = Pessoa.por_ano_nascimento('Helder', 1989)
p1 = Pessoa('Helder', 30)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
