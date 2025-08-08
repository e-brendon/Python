from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        try:
            with open('./1_MVC/pessoas.txt', 'a') as arq:
                arq.write(f"{pessoa.nome}; {pessoa.idade}; {pessoa.cpf}\n")
        except Exception as e:
            print(f"Erro ao salvar pessoa: {e}")
