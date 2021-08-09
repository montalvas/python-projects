from random import randint

class RandomNumber:
    def __init__(self):
        self.guess = 0
        self.min_value = 1
        self.max_value = 100
        self.random_value = 0
    
    
    def Launch(self):
        self.GenerateRandomNumber()
        try:
            self.AskRandomNumber()
        except ValueError:
            print('Precisa ser um número inteiro.')
    
    def AskRandomNumber(self):
        while True:
                self.guess = int(input('Chute um número: '))
                if self.guess > self.random_value:
                    print('>>Chute foi maior que o número.')
                elif self.guess < self.random_value:
                    print('>>Chute foi menor que o número.')
                else:
                    print('>>Parabéns!! você acertou o número!')
                    break    
    
    def GenerateRandomNumber(self):
        self.random_value = randint(self.min_value, self.max_value)


if __name__ == '__main__':
    generator = RandomNumber()
    generator.Launch()