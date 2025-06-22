#nomes = ['brendon', 'caio', 'marcos', 'joao'] #
# index     0         1         2       3 ...
#nomes[0] = 'Brendon Esteves'
#print(nomes)
## usando o método append para adicionar um novo nome
#nomes.append('maria')
#print(nomes)
nomes = []
while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome == '-1':
        print( 'Voce escolheu sair.' )
        break
    else:
        nomes.append(nome)
print('Lista de nomes cadastrados:', nomes)