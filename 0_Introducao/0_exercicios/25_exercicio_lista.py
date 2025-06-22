# receba 10 valores e exiba a soma de todos eles 
valores = []

for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

print(f'A soma dos valores é: {sum(valores)}')

# usando a forma em que usa a logica 

soma = 0
for i in valores:
    soma += i
print(f'A soma dos valores é: {soma}')