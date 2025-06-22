#Escreva um programa que receba notas de um aluno (0 - 10), 
#caso #a nota digitada esteja fora dessa intervalo peça para o professor digitar
#novamente 

nota = float(input("Digite a nota do aluno (0-10): "))

while nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
    nota = float(input("Digite a nota do aluno (0-10): "))
print(f"A nota do aluno é: {nota:.1f}")
