import pickle

x = {
    'nome': 'brendon',
    'idade': '26',
    'é': 'isso'
}

print (type(x))

string = pickle.dumps(x)

print (pickle.loads(string))

y = [1, 2, 3]

arq = open('./0_introducao/0_base/arquivos/aula64.pkl', 'wb')
pickle.dump(y, arq)

arq = open('./0_introducao/0_base/arquivos/aula64.pkl', 'rb')
retorno = pickle.load(arq)
print (retorno)
