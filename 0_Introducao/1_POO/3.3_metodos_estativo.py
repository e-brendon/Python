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
    
    @staticmethod
    def e_adulto(idade):
        if idade >= 18:
            return True
        else:
            return False
        


print (Pessoas.e_adulto(21))  # True
