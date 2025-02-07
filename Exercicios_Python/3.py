class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return (self.altura * 2) + (self.largura * 2)

altura = int(input("Digite a altura do retangulo: "))
largura = int(input("Digite a largura do retangulo: "))

retangulo = Retangulo(altura, largura)

print(retangulo.area())
print(retangulo.perimetro())



    