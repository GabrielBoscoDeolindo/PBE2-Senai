class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

class Banco:
    def __init__(self):
        self.clientes = [] 
        self.contas = []    

    def cadastrar_cliente(self, nome):
        cliente = Cliente(nome)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente

    def abrir_conta(self, cliente):
        conta = Conta(cliente)
        self.contas.append(conta)
        print(f"Conta aberta para {cliente.nome}.")
        return conta

    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem.saldo >= valor and valor > 0:
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor} realizada com sucesso!")
        else:
            print("Transferência não realizada. Verifique o saldo e o valor.")

banco = Banco()
cliente = banco.cadastrar_cliente("Gabriel")
conta = banco.abrir_conta(cliente)

while True:
    print("\nO que deseja fazer?")
    print("[1] Sacar")
    print("[2] Depositar")
    choice = int(input("Escolha uma opção: "))

    if choice == 1:
        saque = float(input("Quanto deseja sacar: "))
        conta.sacar(saque)
        conta.exibir_saldo()
    elif choice == 2:
        deposito = float(input("Quanto deseja depositar?: "))
        conta.depositar(deposito)
        conta.exibir_saldo()
    else:
        print("Opção inválida. Tente novamente.")





