import random

class JogoCartas:
    def __init__(self):
        self.baralho = [f"{cor} {numero}" for cor in ['verde', 'amarelo', 'azul', 'vermelho'] for numero in range(10)]

    def embaralhar(self):
        random.shuffle(self.baralho)

    def distribuir(self, num_jogadores, num_cartas):
        maos = {f"Jogador {i + 1}": [] for i in range(num_jogadores)}
        for i in range(num_cartas):
            for jogador in maos.keys():
                maos[jogador].append(self.baralho.pop(0))  
        return maos

jogo = JogoCartas()
jogo.embaralhar()

print("Cartas: ")
num_jogadores = 2
num_cartas = 7
maos = jogo.distribuir(num_jogadores, num_cartas)

for jogador, cartas in maos.items():
    print(f"{jogador}: {', '.join(cartas)}")


