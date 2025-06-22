# Escreva um programa onde o usuáario informa duas notas e ele mostre a média entre elas 
import os, platform

def clean ():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
clean()

print(f"A média entre {nota1} e {nota2} é: {media:.2f}")

