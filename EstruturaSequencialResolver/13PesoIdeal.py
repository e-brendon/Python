#!/usr/bin/env python3

'''
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
    que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
'''

peso = float (input ('Altura: '))
sexo = input ("Sexo: M ou F: ")

if sexo == "M":
    ideal = (72.7 * pesp) - 58
    print(f"O peso ideal é: {ideal}")
else:
    ideal = (62.1 * peso) - 44.7
    print (f"O peso ideal é: {ideal}")