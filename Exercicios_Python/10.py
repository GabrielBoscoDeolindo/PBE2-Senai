class Livro:
    def __init__(self,titulo,autor,num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def emprestar(self, disponivel):
        if disponivel == True:
            disponivel = False 
            print("Você emprestou o livro")
            return disponivel
        else:
            return print("Livro não está disponível")
    
    def devolver(self, disponivel):
        if disponivel == True:
            print("O livro já foi devolvido")
        else:
            disponivel = True
            print("Obrigado por devolver o livro!")

livro = Livro("HungerGames","SuzanneCollins",200)
disponivel = True
choice = int(input("O que deseja fazer com o livro: [1]Emprestar [2]Devolver: "))
if choice == 1:
    livro.emprestar(disponivel)
elif choice == 2:
    livro.devolver(disponivel)