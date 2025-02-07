class Biblioteca:
    def __init__(self):
        self.cadastros = {}  

    def cadastro(self, titulo, autor):
        if titulo in self.cadastros:
            print(f"O livro '{titulo}' já está cadastrado")
        else:
            self.cadastros[titulo] = {"autor": autor, "disponivel": True}
            print(f"{titulo} adicionado ao cadastro")

    def emprestar(self, titulo):
        if titulo in self.cadastros:
            if self.cadastros[titulo]["disponivel"]:
                self.cadastros[titulo]["disponivel"] = False
                print(f"Você emprestou o livro '{titulo}'")
            else:
                print(f"{titulo} não está disponível.")
        else:
            print(f"{titulo} não está cadastrado na biblioteca.")

    def devolver(self, titulo):
        if titulo in self.cadastros:
            if self.cadastros[titulo]["disponivel"]:
                print(f"O livro '{titulo}' já foi devolvido.")
            else:
                self.cadastros[titulo]["disponivel"] = True
                print(f"Obrigado por devolver o livro {titulo}")
        else:
            print(f"{titulo} não está cadastrado na biblioteca.")

biblioteca = Biblioteca()
while True:
    print("\nO que deseja fazer?")
    print("[1] Cadastrar um livro [2] Emprestar um livro [3] Devolver um livro")
    
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        biblioteca.cadastro(titulo, autor)
    elif escolha == 2:
        titulo = input("Título do livro para emprestar: ")
        biblioteca.emprestar(titulo)
    elif escolha == 3:
        titulo = input("Título do livro para devolver: ")
        biblioteca.devolver(titulo)
    else:
        print("invalido")
