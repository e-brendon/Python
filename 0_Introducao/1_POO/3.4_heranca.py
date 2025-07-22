class Pessoa:
    
    def andar(self):
        print(f"está andando.")
    
    def falar(self):
        print(f"está falando.")
# ----
class Cliente(Pessoa):
    
    def comprar(self):
        print(f"está comprando.")
# ----
class Vendedor(Pessoa):
    
    def vender(self):
        print(f"está vendendo.")
# ----

p1 = Cliente()
v1 = Vendedor()

p1.andar()
p1.falar()
p1.comprar()
print (10* '--**' + '--')
v1.andar()
v1.falar()
v1.vender()