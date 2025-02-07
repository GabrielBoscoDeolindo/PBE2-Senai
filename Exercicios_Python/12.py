class LojaVirtual:
    def __init__(self):
        self.estoque = {}

    
    def cadastro(self, nome, preco):
        self.estoque[nome] = preco
        print(f"{nome} adicionado ao cadastro!")
        print(self.estoque)
    
    def comprar(self, nome):
        if nome in self.estoque:
            if self.estoque[nome] > 10:
                self.estoque[nome] -= 1.00
        else:
            print("Produto não encontrado")
        print(f"Valor do produto pós desconto {self.estoque[nome]}")
    
    

produto = LojaVirtual()
while True:
    choice = int(input("O que deseja fazer? [1]Cadastro [2]Comprar "))
    if choice == 1:
        nome = input("Digite o nome do produto: ")
        preco = int(input("Digite o preco: "))
        produto.cadastro(nome, preco)
    elif choice == 2:
        nome = input("Que produto deseja comprar? ")
        produto.comprar(nome)




