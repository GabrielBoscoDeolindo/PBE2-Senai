import random

class Jogo:
    def __init__(self):
        self.num = random.randint(1, 10)
        self.palpite_atual = None

    def jogar(self):
        while True:
            self.palpite_atual = int(input("Digite um número de 1 a 10: "))
            if self.distancia():
                break
        print("Você venceu!")

    def distancia(self):
        if self.palpite_atual > self.num:
            print("O número correto é menor.")
        elif self.palpite_atual < self.num:
            print("O número correto é maior.")
        else:
            return True 
        return False  

jogo = Jogo()
jogo.jogar()

