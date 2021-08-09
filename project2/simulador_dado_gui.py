from random import randint
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'Você gostaria de gerar um novo valor para o dado? '
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]      
        
    def Iniciar(self):
        self.window = sg.Window('Simulador de Dado', layout=self.layout)
        
        self.eventos, self.valores = self.window.Read()
        
        try:
            if self.eventos == 'sim'or self.eventos == 's':
                self.GenerateDiceValue()
            elif self.eventos == 'não'or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')
    
    def GenerateDiceValue(self):
        value = randint(self.min_value, self.max_value)
        print(value)


if __name__ == '__main__':
    dice = DiceSimulator()
    dice.Iniciar()