#Faça um programa que o usuário possa n pessoas,
#armazenando seu nome, idade e altura
cadrastro = {
    'nomes': [],
    'idades': [],
    'alturas': [],
}

def linha():
    print(30 * '-_')

def cadastrando():
    cadrastro['nomes'].append(input('Digite um nome: '))
    cadrastro['idades'].append(int(input('Digite uma idade: ')))
    cadrastro['alturas'].append(float(input('Digite uma altura: ')))
    linha()

decisao = 'n'   
while True:
    if decisao == 'v':
        for i in range(len(cadrastro['nomes'])):
            print(f"Nome: {cadrastro['nomes'][i]}, Idade: {cadrastro['idades'][i]}, Altura: {cadrastro['alturas'][i]}") 
        linha()
        
    elif decisao == 'n':
        linha()
        cadastrando()
    
    elif decisao == 's':
        linha()
        print ('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    decisao = input('Deseja ver as pessoas cadastradas tecle V, sair Tecle S, Cadastrar uma nova N: ').strip().lower()

print('Programa encerrado.')  # Mensagem de encerramento do programa

