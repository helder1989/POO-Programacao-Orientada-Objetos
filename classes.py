class Escritor:
    def __init__(self, nome):
        self.__nome = nome #  __ atributo privado
        self.__ferramenta = None

    @property  # getters e setters são metodos para controlar (validar) e entrada e saíde de dados dos atrubutos
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):  # uma caneta pode está ou não associada a um escritor ou outra classe
        self.__marca = marca  # __ atributo privado

    @property  # getters e setters são metodos para controlar (validar) e entrada e saíde de dados dos atrubutos
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está digitando...')

