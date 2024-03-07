from random import randrange
y = 0

for i in range(0, 100):
    x = randrange(0, 100)
    print(f'{i} = {x}')
    y += x

print(f'A soma de todos os números aleatórios é {y}')
