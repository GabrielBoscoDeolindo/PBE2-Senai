class Agenda:
    def __init__(self):
        self.agenda = {}

    def adicionar(self, nome, telefone):
        self.agenda[nome] = telefone
        print(f"{nome} adicionado à agenda!")
        print(self.agenda)
    
    def remover(self, nome):
        if nome in self.agenda:
            self.agenda.pop(nome)
            print(f"{nome} removido com sucesso")
            print(self.agenda)
        else:
            print("nome não tá na lista")
    
    def buscar(self,nome):
        if nome in self.agenda:
            print(f"O telefone de {nome} é {self.agenda[nome]}")
        else:
            print("nome não tá na lista")
        
agenda = Agenda()
while True:
    choice = int(input("O que deseja fazer? [1]Adicionar [2]Remover [3]Buscar "))
    if choice == 1:
        nome = input("Digite o nome do contato: ")
        telefone = int(input("Digite o número do contato: "))
        agenda.adicionar(nome, telefone)
    elif choice == 2:
        nome = input("Que contato deseja remover? ")
        agenda.remover(nome)
    elif choice == 3:
        nome = input("Que contato deseja buscar? ")
        agenda.buscar(nome)


