def soma (n1, n2):
    if n1 < 0 or n2< 0:
        raise ValueError("Os números devem ser positivos")
    return n1 + n2

print(soma(10, 20))  # Deve funcionar
print(soma(-10, 20))  # Deve levantar um erro