x = [i for i in range (0, 26)]

x = list(map(lambda x: 10 if x % 2 == 0 else (x), x))

print(x)
