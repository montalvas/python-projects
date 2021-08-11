# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que te dar uma resposta

from random import choice

class DecidaPorMim:
    def __init__(self):
       self.answers = [
           'Com certeza, você deve fazer isso!',
           'Não sei, você que sabe.',
           'Não faz isso não!',
           'Acho que tá na hora certa!'
       ]
    
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(choice(self.answers))


if __name__ == '__main__':
    decida = DecidaPorMim()
    decida.Iniciar()