class Tarefa:
    def __init__(self):
        self.tarefas = {}
    
    def cadastro(self, nome, prioridade, status, vencimento):
        self.tarefas.update({nome: [prioridade, status, vencimento]})
        print(f"{nome} adicionada com sucesso!")
    
    def editar(self, nome):
        if nome in self.tarefas:
            print(f"Editando a tarefa: {nome}")
            prioridade = input("Nova prioridade (pouco, normal, urgente): ")
            status = input("Novo status (nao iniciada, em andamento, pronto): ")
            vencimento = input("Nova data de vencimento: ")
            self.tarefas[nome] = [prioridade, status, vencimento]
            print(f"{nome} atualizada com sucesso!")
        else:
            print(f"{nome} não encontrada.")
    
    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Tarefas cadastradas:")
            for nome, detalhes in self.tarefas.items():
                print(f"- {nome}: Prioridade: {detalhes[0]}, Status: {detalhes[1]}, Vencimento: {detalhes[2]}")
    
    def excluir(self, nome):
        if nome in self.tarefas:
            del self.tarefas[nome]
            print(f"{nome} excluída com sucesso!")
        else:
            print(f"{nome} não encontrada.")

tarefa = Tarefa()
while True:
    choice = int(input("O que você deseja fazer? [1]Criar [2]Editar [3]Listar [4]Excluir: "))
    if choice == 1:
        nome = input("Dê um nome para a tarefa: ")
        prioridade = input("Dê uma prioridade (pouco, normal, urgente): ")
        status = input("Qual o status da tarefa (nao iniciada, em andamento, pronto): ")
        data_vencimento = input("Quando precisa ser entregue: ")
        tarefa.cadastro(nome, prioridade, status, data_vencimento)
    elif choice == 2:
        nome = input("Qual o nome da tarefa que deseja editar? ")
        tarefa.editar(nome)
    elif choice == 3:
        tarefa.listar()
    elif choice == 4:
        nome = input("Qual o nome da tarefa que deseja excluir? ")
        tarefa.excluir(nome)
    else:
        print("Opção inválida. Tente novamente.")
