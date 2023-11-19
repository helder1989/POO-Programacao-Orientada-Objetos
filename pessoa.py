from datetime import datetime
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) # é uma variavel, atributo de class
    def __init__(self, nome, idade, comendo=False, falando=False ): # parametros e seus valores
        self.nome = nome # variavel da instancia
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto): # recebendo o parametro assunto pra ele falar
        if self.comendo: # antes de pedir pra ele falar estamos verificando a variavel comendo primeiro
            print(f'{self.nome} não pode falar de boca cheia.')
            return

        if self.falando: # verificando se ele está falando, antes de configurar a minha variavel falando
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando {assunto}.')
        self.falando = True      # configurando a váriavel falando

    def parar_falar(self): # preciso determinar que essa variavel falando seja false em algum momento
        if not self.falando:
            print(f'{self.nome} não está falando') # mensagem de erro ao usuário
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False  # mudando o status da variavel falando


    def comer(self, alimento): # estamos pedindo para a classe Pessoa comer
        if self.comendo:
            print(f'{self.nome} já está comendo.') # mensagem ao usuário
            return

        if self.falando: # verificando se está falando
            print(f'{self.nome} não pode comer falando.')
            return


        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True  # mudando o status da variavel comendo

    def parar_comer(self): # preciso determinar que essa variavel comendo seja false em algum momento
        if not self.comendo:
            print(f'{self.nome} não está comendo.') # mensagem de erro ao usuário
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False # mudando o status da variavel comendo

    def get_ano_nascimento(self): # utiliza um atributo da class e da instancia
        return self.ano_atual - self.idade


