try:
    x = int (input("Digite um número: "))

    print (5/x)
except ValueError:
    print('digite um numero inteiro mermão \n')
except ZeroDivisionError:
    print('po mano, não pode ser zero mermão')
