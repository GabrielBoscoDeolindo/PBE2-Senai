class RedeSocial:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []
        self.posts = {}
        self.comentarios = []
    def adicionar(self, nome):
        if nome in self.nome:
            if nome in self.amigos:
                print("Esse amigo já está na sua lista")
            else:
                print(f"{nome} foi adicionado a sua lista de amigos!")
                self.amigos.append(nome)
                print(self.amigos)
        else:
            print("Usuário não encontrado")
    
    def publicar(self, nome):
        if nome in self.nome:
            nome_post = input("Digite o nome do post: ")
            post = input("Conteúdo do post: ")
            self.posts[nome_post] = post
            print(self.posts)
        else:
            print("Usuário não encontrado")
    
    def comentar(self, nome):
        if nome in self.nome:
            nome_post = input("Digite o nome do post: ")
            if nome_post in self.posts:
                comentario = input("Digite seu comentário: ")
                self.comentarios.append(comentario)
                print(self.comentarios)
            else:
                print("Post não encontrado")
        else:
            print("Usuário não encontrado")
    
    def buscar(self, nome):
        if nome in self.nome:
            print(f"{nome} é um usuário cadastrado")
        else:
            print("Usuário não encontrado")
    
conta1 = "Gabriel"
conta2 = "Maria"
conta3 = "Ritcher"
contas = RedeSocial([conta1, conta2, conta3])
while True:
    choice = int(input("O que deseja fazer? [1]Buscar [2]Add amigo [3]Publicar [4]Comentar "))
    if choice == 1:
        nome = input("Digite o nome do contato: ")
        contas.buscar(nome)
    elif choice == 2:
        nome = input("Digite o nome do contato: ")
        contas.adicionar(nome)
    elif choice == 3:
        nome = input("Quem deseja publicar: ")
        contas.publicar(nome)
    elif choice == 4:
        nome = input("Quem deseja comentar: ")
        contas.comentar(nome)