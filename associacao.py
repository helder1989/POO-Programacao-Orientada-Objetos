  # relação entre classes, aonde uma classe não depende da outra

from classes import Escritor  # importando a classe Escritor a partir do modelo classes.py
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()



