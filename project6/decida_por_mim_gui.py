# Projeto 6 - Projeto 5 com interface gráfica

from random import choice
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
       self.answers = [
           'Com certeza, você deve fazer isso!',
           'Não sei, você que sabe.',
           'Não faz isso não!',
           'Acho que tá na hora certa!'
       ]
       
    def Iniciar(self):
        self.layout = [
           [sg.Text('Faça sua pergunta:', size=(40, 0))],
           [sg.Input()],
           [sg.Button('Decida por mim')],
           [sg.Button('Fechar')],
           [sg.Output(size=(40, 0))]
       ]
    
        self.window = sg.Window('Decida por mim', layout=self.layout)
        
        while True:
            self.event, self.value = self.window.Read()
        
            if self.event == 'Decida por mim':
                print(choice(self.answers))
            elif self.event == 'Fechar':
                break


if __name__ == '__main__':
    decida = DecidaPorMim()
    decida.Iniciar()