x = [i for i in range(0, 10)]

print(x)

# ----
# pegando nomes 
y = [input ('Digite um nome: ') for i in range(3)]

print(y)

print ('Construindo uma matrz')

z = [ [j for j in range(4, 7) ] for k in range(0, 3) ]

print(z)

# com condicional 
h = [b for b in range(0, 10) if b % 2 == 0]
print (h)