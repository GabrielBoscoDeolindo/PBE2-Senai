class Triangulo:
    def __init__(self,altura,l1,l2,l3):
        self.altura = altura
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def validade(self):
        if self.l1+self.l2>=self.l3 and self.l2+self.l3>=self.l1 and self.l3+self.l1>=self.l2:
            return True
        else:
            return False
    
    def area(self):
        return (self.altura * self.l2) / 2

triangulo = Triangulo(10,10,10,10)
print(f"O triangulo é válido? {triangulo.validade()}")
print(f"Sua área é: {triangulo.area()}")