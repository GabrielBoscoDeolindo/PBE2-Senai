class Cliente:
    def __init__(self, nome):
        self.nome = nome
        
class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")

    def sacar(self, valor):
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class Banco:
    def __init__(self):
  
    def cadastrar_cliente(self, nome):
        print(f"Cliente {nome} cadastrado com sucesso!")

    def abrir_conta(self, cliente):
        return print(f"Conta aberta para {cliente.nome}.")

    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem.saldo >= valor and valor > 0:
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
        else:
            print("Transferência não realizada. Verifique o saldo e o valor.")

banco = Banco()
cliente = banco.cadastrar_cliente("Gabriel")
conta = banco.abrir_conta(cliente)

while True:
    choice = int(input("O que deseja fazer? [1]Sacar [2]Depositar: "))
    if choice == 1:
        saque = int(input("Quanto deseja sacar: "))
        conta.sacar(saque)
        conta.exibir_saldo()
    else:
        deposito = int(input("Quanto deseja depositar?: "))
        conta.depositar(deposito)
        conta.exibir_saldo()





