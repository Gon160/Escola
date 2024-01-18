while True:
    X = int(input('Digite um valor x: '))
    if 1 > X < 100:
        print('Valor invalido volte a tentar')
    else:
        break

while True:
    Y = int(input('Digite um valor y: '))
    if 1 > Y < 100 or X > Y:
        print('Valor invalido volte a tentar')
    else:
        break

for i in range(X, Y+1):
    if i % 2 != 0:
        print(i)
