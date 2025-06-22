x = [12, 14, 15, 16, 17, 18, 19, 20]

x = list(filter(lambda x: x < 18 or x % 2 == 0, x))

print(x)