class Funcionario:
    def __init__(self,nome,salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def desconto(self, plano_saude, vale, imposto):
        return self.salario - plano_saude - vale - imposto

salario_bruto = int(input("Digite seu salário: "))
dados = Funcionario("Gabriel",salario_bruto,"TI")
print(dados.desconto(100, 100, 100))