class Pessoa:
    
    def __init__ (self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
# ----
class Cliente(Pessoa):
    
    def __init__ (self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
# ----
class Vendedor(Pessoa):
    def __init__(self,id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor
# ----

print (4* "-" + 'cliente' + 4* "-")
c1 = Cliente(1, "João", "123.456.789-00")
print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)

print (4* "-" + 'Vendedor' + 4* "-")
v1 = Vendedor(2, "Maria", "987.654.321-00")
print(v1.id_vendedor)
print(v1.nome)
print(v1.cpf)
