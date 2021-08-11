# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Qual é o cenário : Eu estou numa guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer, e o ladoB irá perder! então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente o ladoA irá conseguir!

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
        self.resposta1 = input(self.pergunta1).lower()
        if self.resposta1 == 'norte':
            self.resposta2 = input(self.pergunta2).lower()
            if self.resposta2 == 'espada':
                print(self.final_historia1)
            elif self.resposta2 == 'arco':
                print(self.final_historia2)
        elif self.resposta1 == 'sul':
            self.resposta3 = input(self.pergunta3).lower()
            if self.resposta3 == 'linha de frente':
                print(self.final_historia3)
            elif self.resposta3 == 'tatico':
                print(self.final_historia4)


if __name__ == '__main__':
    game = AdventureGame()
    game.Play()