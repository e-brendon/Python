#Receba uma temperatura em farenheit e exiba em graus celsius.
#c=5 * f - 32/9

farenaheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (farenaheit - 32) * 5 / 9
print(f"A temperatura em Celsius é: {celsius:.2f}°C")
