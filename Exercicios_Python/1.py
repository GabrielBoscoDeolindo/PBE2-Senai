import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

circulo = Circulo(10)  
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Perímetro: {circulo.calcular_perimetro():.2f}")
