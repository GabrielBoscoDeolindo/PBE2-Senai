class ContaBancaria:
    def __init__(self,num_conta,nome,saldo = 1000):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        return self.saldo

    def sacar(self, saque):
        self.saldo -= saque
        return self.saldo

conta = ContaBancaria(212131123, "gabriel")

escolha = int(input("Digite o que deseja realizar: [1]Deposito [2]Saque: "))
if escolha == 1:
    deposito = float(input("Digite quanto deseja depositar: "))
    print(f"Seu saldo agora é: {conta.depositar(deposito)}")
elif escolha == 2:
    saque = float(input("Digite quanto deseja sacar: "))
    print(f"Seu saldo agora é: {conta.sacar(saque)}")
else:
    print("Opção inválida!")