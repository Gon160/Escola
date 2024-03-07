from random import randrange

x = randrange(0, 100)

if x % 2 == 0:
    print(f'O número {x} é par')
else:
    print(f'O numero {x} é impar')