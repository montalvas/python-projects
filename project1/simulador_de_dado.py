# Projeto 1 - Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

from random import randint

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'Você gostaria de gerar um novo valor para o dado? '
    
    def Iniciar(self):
        try:
            answer = input(self.message).lower()
            if answer == 'sim' or answer == 's':
                print(f'Valor gerado: {self.GenerateDiceValue()}')
            elif answer == 'não' or answer == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')
    
    def GenerateDiceValue(self):
        value = randint(self.min_value, self.max_value)
        return value


if __name__ == '__main__':
    dice = DiceSimulator()
    dice.Iniciar()