#!/usr/bin/env python3

'''
	Faça um Programa que peça as 4 notas bimestrais e mostre a média
'''
cont = 1
media = 0
for i in range(4):
	nota = float (input(f'{cont}° Digite a nota: '))
	media += nota
	cont += 1
print(f'A nota da média final é: {media/4}\n')