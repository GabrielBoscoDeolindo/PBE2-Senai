class Character:
    def __init__(self,nome, saude,forca,defesa,habilidades):
        self.nome = nome
        self.saude = saude
        self.forca = forca
        self.defesa = defesa
        self.habilidades = habilidades
    
    def combate(self, adversario):
        while self.saude > 0 and adversario.saude > 0:
            dano = self.forca - adversario.defesa
            adversario.saude -= dano
            print(f"{self.nome} ataca {adversario.nome} causando {dano} de dano!")
            print(f"Vida da Zelda: {adversario.saude}\n")

            dano = adversario.forca - self.defesa
            self.saude -= dano
            print(f"{adversario.nome} ataca {self.nome} causando {dano} de dano!")
            print(f"Vida do Link: {self.saude}\n")

            if self.saude <= 0:
                print(f"{adversario.nome} venceu!")
                break

            if adversario.saude <= 0:
                print(f"{self.nome} venceu!")
                break
        
        
link = Character("link",50, 18, 10, "Corage")
zelda = Character("zelda",50, 13, 12, "Wisdom")
link.combate(zelda)

