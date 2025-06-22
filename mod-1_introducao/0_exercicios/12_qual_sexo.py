#Receba F para feminimo e M para masculino e exbia o sexo da pessoa

sexo = str (input("Digite o sexo (F/M): ")).strip().upper()

if sexo == "F":
    sexo = "Feminino"
elif sexo == "M":
    sexo = "Masculino"
else:
    sexo = "Inválido"

print (f"O sexo informado foi: {sexo} !")