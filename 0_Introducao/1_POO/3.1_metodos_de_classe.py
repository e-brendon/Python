class Pessoas:
    possui_olhos = True  # Atributo de classe
    possui_boca = True  # Atributo de classe
    raca = 'Humano'  # Atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def retorna_nome(self):
        return self.nome
    
    def loga_sistema(self):
        print(f"{self.retorna_nome()} está logado no sistema.")
    
    @classmethod
    def andar(cls, vlc):
        print( f'estou andando, com {vlc} km/h' )
        
p1 = Pessoas('João', 30)
p2 = Pessoas('Maria', 25)
#p1.loga_sistema()
#p1.andar()

Pessoas.andar(10)

#print(f"Nome: {p1.nome}, Idade: {p1.idade}, Raça: {p1.raca}")

