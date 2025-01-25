class Tarefa:
    def __init__(self):
        self.tarefas = {}
    
    def cadastro(self,nome,prioridade,status,vencimento):
        self.tarefas.update({nome: [prioridade,status,vencimento]})
        print(self.tarefas)

tarefa = Tarefa()
choice = int(input("O que você deseja fazer? [1]Criar [2]Editar [3]Listar [4]Excluir: "))
if choice == 1:
    nome = input("Dê um nome para a tarefa: ")
    prioridade = input("Dê uma prioridade (pouco, normal, urgente): ")
    status = input("Qual o status da tarefa (nao iniciada, em andamento, pronto): ")
    data_vencimento = input("Quando precisa ser entregue: ")
    tarefa.cadastro(nome, prioridade, status, data_vencimento)
elif choice == 2: