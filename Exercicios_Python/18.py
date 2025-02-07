import calendar
from datetime import datetime

class Calendario:
    def __init__(self, feriados=None):
        self.feriados = set(feriados) if feriados else set()

    def exibir_mes(self, ano, mes):
        print(calendar.month(ano, mes))

    def verificar_feriado(self, data):
        return data in self.feriados

    def diferenca_dias(self, data1, data2):
        d1 = datetime.strptime(data1, "%d/%m/%Y")
        d2 = datetime.strptime(data2, "%d/%m/%Y")
        return (d2 - d1).days

feriados = ["01/01/2025", "25/12/2025", "07/09/2025"]
calendario = Calendario(feriados)

mes = int(input("Digite um mes (numero): "))
if mes <= 12:
    calendario.exibir_mes(2025, mes)
else:
    print(erro)

data = "25/12/2025"
if calendario.verificar_feriado(data):
    print(f"{data} é um feriado!")
else:
    print(f"{data} não é um feriado.")

data1 = "01/01/2025"
data2 = "25/12/2025"
diferenca = calendario.diferenca_dias(data1, data2)
print(f"A diferença entre {data1} e {data2} é de {diferenca} dias.")
