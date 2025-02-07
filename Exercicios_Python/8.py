class Carro:
    def __init__(self, marca, cor, velocidade):
        self.marca = marca
        self.cor = cor
        self.velocidade = velocidade
    
    def acelerar(self, acelerar):
        self.velocidade += acelerar

    def frear(self, frear):
        self.velocidade -= frear

    def speed_atual(self):
        return f"Sua velocidade atual é: {self.velocidade} km/h"

carro = Carro("Toyota", "Verde", 150)

escolha = int(input("O que você deseja fazer? [1]Acelerar [2]Frear: "))
if escolha == 1:
    acelerar = int(input("Quanto você quer acelerar? "))
    carro.acelerar(acelerar) 
    print(carro.speed_atual())  
elif escolha == 2:
    frear = int(input("Quanto você quer frear? "))
    carro.frear(frear)  
    print(carro.speed_atual())  
else:
    print("Opção inválida!")
