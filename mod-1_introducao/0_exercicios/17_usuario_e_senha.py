#Defina um usuário e senha e depois verifique se
#login do usuário é valido 

usuario = "admin"
senha = 'senhaforte123'
tentativas = 0

while True:
    usuario_input = input("Digite o usuário: ")
    senha_input = input("Digite a senha: ")

    if usuario_input == usuario and senha_input == senha:
        print("Login bem-sucedido!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        tentativas += 1
        if tentativas >= 3:
            print("Número máximo de tentativas excedido. Acesso negado.")
            break
        else:
            print(f"Você tem {3 - tentativas} tentativas restantes.")
            

