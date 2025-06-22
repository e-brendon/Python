
k = 0
for i in range(0, 30):
    print (f"{i}°{4*"--*"}")
    for j in range(0, 30):
        print(f"i: {i}, j: {j}")  # Linha de separação entre iterações de i
        k += 1
print(f"Total de iterações: {k}")