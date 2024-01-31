#Escreva um programa que peça ao utilizador um número inteiro n entre 1 e 100,
#inclusive. A leitura dos dados e respetiva validação devem ser feitas numa função com
#o seguinte protótipo:
#def readData()
#que devolve o inteiro lido. O programa deve mostrar no ecrã os múltiplos de 3, desde n
#até 121, usando para isso uma função com o seguinte protótipo:
#def multipleOf3(n).
def readData():
    while True:
        x = int(input("Insira um numero entre 1 e 121: "))
        if 1 <= x <= 121:
            return x
            break
        else:
            print("Valor invalido!")


def Multiplo3(x):
    for i in range(x, 122):
        if i % 3 == 0:
            print(i)


x = readData()
Multiplo3(x)
