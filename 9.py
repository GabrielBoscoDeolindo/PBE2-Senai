class Paciente:
    def __init__(self,nome,idade,historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico
    
    def add_consulta(self):
        consulta = input("Que consulta quer adicionar ao histórico: ")
        self.historico.append(consulta)
        return consulta

paciente = Paciente("Gabriel", 19, ["Oftalmo", "Pediatra", "Dermato"])
paciente.add_consulta()

print(f"Histórico de consultas: {paciente.historico}")
