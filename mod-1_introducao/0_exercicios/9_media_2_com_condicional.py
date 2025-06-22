# media de aluno com condicional

import os, platform 
def clean():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
clean()

if media >= 7:
    print(f"Aprovado com média {media:.2f}")
    if media == 10:
        print("Parabéns, você tirou 10!")
    if media > 10:
        print("Einstein junior ?.")
        
elif media >= 5:
    print(f"Recuperação com média {media:.2f}")
    
else:
    print(f"Reprovado com média {media:.2f}")