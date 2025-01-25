class Ecommerce:
    def __init__(self):
        self.produtos = {}
        self.clientes = {}
        self.pedidos = []

    def adicionar_produto(self, nome, preco, categoria, estoque):
        self.produtos[nome] = {"preco": preco, "categoria": categoria, "estoque": estoque}
        print(f"Produto '{nome}' adicionado com sucesso.")

    def listar_produtos(self):
            print("Produtos disponíveis: ")
            for nome, detalhes in self.produtos.items():
                print(f"{nome}: R$ {detalhes['preco']}, Estoque: {detalhes['estoque']}, Categoria: {detalhes['categoria']}")

    def adicionar_cliente(self, nome, email, endereco):
        self.clientes[email] = {"nome": nome, "endereco": endereco, "historico": []}
        print(f"Cliente '{nome}' cadastrado com sucesso.")

    def criar_carrinho(self, email):
        return {"cliente": email, "itens": [], "frete": 0.0}

    def adicionar_ao_carrinho(self, carrinho, nome_produto, quantidade):
        if self.produtos[nome_produto]["estoque"] < quantidade:
            print("Estoque insuficiente.")
        else:
            self.produtos[nome_produto]["estoque"] -= quantidade
            carrinho["itens"].append({"produto": nome_produto, "quantidade": quantidade})
            print(f"{quantidade}x '{nome_produto}' adicionado ao carrinho.")

    def calcular_total_carrinho(self, carrinho):
        subtotal = sum(self.produtos[item["produto"]]["preco"] * item["quantidade"] for item in carrinho["itens"])
        return subtotal + carrinho["frete"]

loja = Ecommerce()

loja.adicionar_produto("Celular", 1500.00, "Eletrônicos", 10)
loja.listar_produtos()
loja.adicionar_cliente("gabriel", "gabriel@email.com", "rua")
carrinho = loja.criar_carrinho("gabriel@email.com")
loja.adicionar_ao_carrinho(carrinho, "Celular", 2)
carrinho["frete"] = 50.00
print(f"Total do carrinho: R$ {loja.calcular_total_carrinho(carrinho)}")


