class MaquinaVenda:
    def __init__(self):
        self.estoque = {}

    def cadastro(self, nome, preco):
        self.estoque[nome] = preco
        print(f"{nome} adicionado ao cadastro!")
        print(self.estoque)
    
    def compra(self, nome, dinheiro):
        if nome in self.estoque:
            print(f"{nome} custa {self.estoque[nome]}")
            troco = dinheiro - preco 
            return troco
        else:
            print("nome não tá na lista")
        
produto = MaquinaVenda()
while True:
    choice = int(input("O que deseja fazer? [1]Cadastro [2]Comprar "))
    if choice == 1:
        nome = input("Digite o nome do produto: ")
        preco = int(input("Digite o preco: "))
        produto.cadastro(nome, preco)
    elif choice == 2:
        nome = input("Que produto deseja comprar? ")
        dinheiro = int(input("Quanto dinheiro vai inserir? "))
        troco = produto.compra(nome, dinheiro)
        print(f"seu troco é {troco}")

