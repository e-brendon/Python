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
    def andar(cls):
        cls.pernas = 2
        return None
        
p1 = Pessoas('João', 30)
p2 = Pessoas('Maria', 25)

print (Pessoas.possui_boca)
Pessoas.andar()
print (Pessoas.pernas)
