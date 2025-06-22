# maior que ?

numero1 = int (input("Digite o primeiro número: "))
numero2 = int (input("Digite o segundo número: "))
numero3 = int (input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("O maior número é:", numero3)
else:
    print(f"Todos os números são iguais ou não há um único maior. {numero1}")
