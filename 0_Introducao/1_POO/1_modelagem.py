class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def logar_sistema(self):
        print (f'{self.nome} está logado')
    
p1 = Pessoas('Brendon Esteves', 21, '12312312354')
p2 = Pessoas('Python doido', 20, '212121212121')

print (p1.nome, p1.idade, p1.cpf )
p1.logar_sistema()
