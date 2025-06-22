# #Receba um número do usuário e mostra a tabuada desse número
import os, platform
# Limpa a tela do terminal
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# recebe o número do usuário        
number = int (input ("Disk an number: \n:"))
clear_screen()

def tabuada(n):
    for i in range(0, 11):
        print(f"{n} x {i} = {n * i}")
tabuada(number)