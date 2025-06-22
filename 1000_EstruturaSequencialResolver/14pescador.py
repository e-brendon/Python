#!/usr/bin/env python3

'''
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
    rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
    que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça 
    um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar 
    na variável excesso a quantidade de quilos além do limite e na variável multa o 
    valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens 
    adequadas.
'''

rendimento = float (input ("Rendimento em KGs do dia: "))
if rendimento > 50:
    exedeu = rendimento - 50
    multa  = exedeu * 4
else:
    exedeu = 0
    multa  = 0
print (f'''
=+=+Controle diario de João=+=+

Rendimento do dia : {rendimento} KKGs
Excesso           : {exedeu} KGs
Multa             : {multa} R$

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
''')