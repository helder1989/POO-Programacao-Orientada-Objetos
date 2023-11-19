from pessoa import Pessoa

p1 = Pessoa('Helder', 34)
p2 = Pessoa('Kevin', 11)
p3 = Pessoa('Taciane', 22)

print(p1.get_ano_nascimento())  # saber o ano de nascimento levando em consideração a idade
print(p2.get_ano_nascimento())
print(p3.get_ano_nascimento())

# os objetos são independentes um do outro
