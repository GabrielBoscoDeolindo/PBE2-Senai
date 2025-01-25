class Produto:
    def __init__(self, nome, preco_compra, preco_venda, categoria, quantidade=0):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.categoria = categoria
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de {self.nome}. Estoque atual: {self.quantidade}")

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            print(f"Erro: Não há estoque suficiente de {self.nome}. Estoque atual: {self.quantidade}")
        else:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades removidas do estoque de {self.nome}. Estoque atual: {self.quantidade}")

    def alterar_precos(self, novo_preco_compra=None, novo_preco_venda=None):
            self.preco_compra = novo_preco_compra
            print(f"Preço de compra de {self.nome} alterado para {self.preco_compra:}")
            self.preco_venda = novo_preco_venda
            print(f"Preço de venda de {self.nome} alterado para {self.preco_venda:}")

    def exibir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço de Compra: {self.preco_compra:}")
        print(f"Preço de Venda: {self.preco_venda}")
        print(f"Quantidade em Estoque: {self.quantidade}")

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.produtos:
            print(f"Produto {produto.nome} já existe no estoque.")
        else:
            self.produtos[produto.nome] = produto
            print(f"Produto {produto.nome} adicionado ao estoque.")

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f"Produto {nome} removido do estoque.")
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            print("Produtos no estoque:")
            for produto in self.produtos.values():
                produto.exibir_informacoes()

estoque = Estoque()

produto1 = Produto("Celular", 500.00, 800.00, "Eletrônicos", 10)
produto2 = Produto("Notebook", 1500.00, 2500.00, "Informática", 5)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.listar_produtos()
produto1.adicionar_estoque(5)
produto1.remover_estoque(3)
produto1.alterar_precos(novo_preco_venda=850.00)


