from controller import PessoaController

while True:
    decisao = int(input('1 - Cadastrar Pessoa \n' 
                        '2 - Listar Pessoas \n'
                        '0 - Sair\n:' ))
    #decisao para sair ou continuar
    if decisao == 0:
        break
    if decisao < 0 or decisao > 2:
        print('Opção inválida!')
        continue
    # entrada de dados 
    if decisao == 1:
        nome    = input('Digite o nome: ')
        idade   = int(input('Digite a idade: '))
        cpf     = input('Digite o CPF: ')
        # chamando controller para cadastro
        try:
            if PessoaController.Cadastrar(nome, idade, cpf):
                print('Pessoa cadastrada com sucesso!')
            else:
                print('Dados inválidos para cadastro!')
        except:
            print('Erro ao cadastrar pessoa!')
    # saida de informações
    elif decisao == 2:
        try:
            with open('./1_MVC/pessoas.txt', 'r') as arq:
                pessoas = arq.readlines()
                if not pessoas:
                    print('Nenhuma pessoa cadastrada.')
                else:
                    for pessoa in pessoas:
                        nome, idade, cpf = pessoa.strip().split('; ')
                        print(f'Nome: {nome}, Idade: {idade}, CPF: {cpf}')
        except FileNotFoundError:
            print('Arquivo de pessoas não encontrado. Nenhuma pessoa cadastrada.')