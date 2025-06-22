from pympler.asizeof import asizeof

def dobro (lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i * 2)
    return lista_dobro

x = asizeof(dobro(range(0, 100)))

print(x)

#usando o prover 

def dobro_gen ():
    i = 0
    while True:
        yield i
        i += 1
x = dobro_gen()

for j in range (0, 100000):
    print(next(x) * 2) 

