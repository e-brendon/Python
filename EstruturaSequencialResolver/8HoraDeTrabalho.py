#!/usr/bin/env python3

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
e mostre o total do seu salário no referido mês. '''

ganho = float (input ('Quanto você ganha por hora: '))
hora  = float (input ('Quantas horas você trabalha por mês: '))

print(f'Ganhará no fim do mês: {hora *ganho}R$\n')