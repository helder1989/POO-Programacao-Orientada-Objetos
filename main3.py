# Atributos de classes ou variaveis de classes

class Helder:
    nome = 'Silva'  # variaveis de classes disponiveis para todas as intâncias da classe
    nome2 = 'Claudio'
    idade = '34'


Helder1 = Helder()
Helder2 = Helder()

print(Helder1.nome)
print(Helder2.idade)
print(Helder.nome2) # chamando direto a minha class