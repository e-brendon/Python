x = {
    'nomes': [],
    'idades': [],
}
for i in range(3):
    
    x['nomes'].append(input('Digite um nome: '))
    x['idades'].append(int(input('Digite uma idade: ')))

for pessoa in x:
    print(f"{pessoa.capitalize()}: {x[pessoa]}")
    
