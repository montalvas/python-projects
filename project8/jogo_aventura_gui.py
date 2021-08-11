# Projeto 8 - Projeto 7 com interface gráfica

import PySimpleGUI as sg

class AdventureGame:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou Sul? ' # norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou o arco? ' # espada = Lado1, arco = Lado2
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico): ' # linha de frente = Lado1, tático = Lado2
        self.final_historia1 = 'Você será um heroi imparável.'
        self.final_historia2 = 'Você será um heroi com uma mira implacável.'
        self.final_historia3 = 'Você morrerá na batalha final.'
        self.final_historia4 = 'Você teve que fugir e viver renegado.'
    
    def Play(self):
        self.layout = [
            [sg.Output(size=(50, 0))],
            [sg.Input(size=(50, 0), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder'), sg.Button('Parar')]
        ]
        
        self.window = sg.Window('Adventure Game', layout=self.layout)
        
        while True:
            self.LerValores()
            
            if self.event == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()

                if self.values['escolha'].lower() == 'norte':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.values['escolha'].lower() == 'espada':
                        print(self.final_historia1)
                    elif self.values['escolha'].lower() == 'arco':
                        print(self.final_historia2)
                elif self.values['escolha'].lower() == 'sul':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.values['escolha'].lower() == 'linha de frente':
                        print(self.final_historia3)
                    elif self.values['escolha'].lower() == 'tatico':
                        print(self.final_historia4)
            
            if self.event == 'Parar':
                break
        
    def LerValores(self):
            self.event, self.values = self.window.Read()

if __name__ == '__main__':
    game = AdventureGame()
    game.Play()