from model import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open("categoria.txt", 'a') as arq:
            arq.writelines(f"{categoria.categoria}\n")
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
            cls.categoria = list(map(lambda x: x.replace('\n',''), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
        
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            nome_item = getattr(venda.itensVendidos, 'nome', str(venda.itensVendidos))
            preco_item = getattr(venda.itensVendidos, 'preco', '')
            vendedor = venda.vendedor.nome if hasattr(venda.vendedor, 'nome') else str(venda.vendedor)
            comprador = venda.comprador.nome if hasattr(venda.comprador, 'nome') else str(venda.comprador)
            quantidade = getattr(venda, 'quantidadeVendida', getattr(venda, 'quantidadeVendidas', ''))
            arq.writelines(f"{nome_item} | {vendedor} | {comprador} | {preco_item} | {quantidade} | {venda.data}\n")
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            cls.venda = list(map(lambda x: x.replace('\n',''), cls.venda))
            cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vendeu = []
        for i in cls.venda:
            vendeu.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
            return vendeu
            