class Aluno:
    def __init__(self,nome,matricula,notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def media(self, num_notas):
        self.notas = (sum(self.notas) / num_notas)
        return self.notas
    
    def situacao(self,media):
        if media >= 7:
            print("Aprovado")
        elif media >=4:
            print("Recuperacao")
        else:
            print("Reprovado")
            
num_notas = int(input("Digite quantas notas deseja registrar: "))
notas = []
for i in range(num_notas):
    nota = int(input("Digite a nota do aluno: "))
    notas.append(nota)

dados_aluno = Aluno("Gabriel",1322,notas)
media = (dados_aluno.media(num_notas))
print(media)

dados_aluno.situacao(media)
