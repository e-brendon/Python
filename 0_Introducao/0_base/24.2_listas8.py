# a estrutura de dados 

x = [1, 2, 3]       #lista principal
y = x               #aqui ele referencia o mesmo objeto na memoria 
z = x.copy()        #aqui ele cria uma copia do objeto na memoria
z[1] = 'Ola'        #ser diferente alterando um elemento

print(x)
print(y)
print(z)    
