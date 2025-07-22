from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('./1_MVC/pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    
    def ler(self):
        nome =  'Brendon'
        idade = 30
        cpf = '123.456.789-00'    
        return Pessoa(nome, idade, cpf)

p1 = Pessoa('Brendon', 30, '123.456.789-00')
PessoaDal.salvar(p1)