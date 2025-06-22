# Entrada e saidas de dados
import os, platform

def clean ():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# input data from user
age = int(input("Write your age: "))
name = input(str("Write your name here: "))

clean()
result = f"Hello: {name}, Your age is: {age}! \n"
"Have a nice day today!"
print (result)
