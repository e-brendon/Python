def soma_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    print (total)
    
def soma_kwargs(**kwargs):
    total = 0
    for numero in kwargs.values():
        total += numero
    print(total)
    
soma_numeros(10, 1, 10, 2, 4)
soma_kwargs(a=10, b=1, c=10, d=2, e=4)

