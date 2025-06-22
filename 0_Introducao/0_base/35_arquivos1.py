arquivo = open('./mod-1_introducao/0_base/arquivos/aula63.txt', 'a')

i = 0

while True:
    if i > 1:
        break
    
    nome = input ("Digite aqui o nome: ")
    arquivo.write(nome + '\n')
    i += 1
    

arquivo_opn = open('./mod-1_introducao/0_base/arquivos/aula63.txt', 'r')
leitura = arquivo_opn.read()

print (leitura)