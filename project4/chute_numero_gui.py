from random import randint
import PySimpleGUI as sg

class RandomNumber:
    def __init__(self):
        self.guess = 0
        self.min_value = 1
        self.max_value = 100
        self.random_value = 0
    
    
    def Launch(self):
        self.layout = [
            [sg.Text('Seu chute', size=(20, 0))],
            [sg.Input(size=(18, 0), key='guess')],
            [sg.Button('Chutar')],
            [sg.Output(size=(30, 10))]
        ]
        
        self.window = sg.Window('Chute o número!', layout=self.layout)
        
        self.GenerateRandomNumber()
        
        try:
            while True:
                self.event, self.values = self.window.Read()
                
                if self.event == "Chutar":
                    self.guess = int(self.values['guess'])
                    
                    if self.guess > self.random_value:
                        print('Chute foi maior que o número.')
                    elif self.guess < self.random_value:
                        print('Chute foi menor que o número.')
                    else:
                        print('PARABÉNS! você acertou!')
                        break
        except:
            print('Precisa ser um número inteiro.')   
    
    def GenerateRandomNumber(self):
        self.random_value = randint(self.min_value, self.max_value)


if __name__ == '__main__':
    generator = RandomNumber()
    generator.Launch()