def readData():
    while True:
        x = int(input("Insira um numero entre 1 e 121: "))
        if 1 <= x <= 121:
            return x
            break


def Multiplo3(x):
    for i in range(x, 122):
        if i % 3 == 0:
            print(i)


x = readData()
Multiplo3(x)
