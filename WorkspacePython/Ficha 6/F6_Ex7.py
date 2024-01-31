 # Acrescente um menu ao programa do exercício 5, de forma a ficarem disponíveis as
# operações programadas nos exercícios 5 e 6 e também as que são sugeridas de seguida.
# Deverá implementar todas as funcionalidades em forma de funções com os seguintes
# protótipos). O aviso mostrado deve ser adequado a cada caso:
# • uma função que devolva 1 se o carater lido for um número e 0 nos restantes
# casos, com protótipo
# def isNumber(char x):
# • uma função que devolva 1 se o carater lido for uma letra e 0 nos restantes casos,
# cujo protótipo é
# def isAlpha(char x):
# • uma função que devolva 1 se o carater lido for um número ou uma letra e 0 nos
# restantes casos (pode e deve chamar as duas funções anteriores na
# implementação desta). O protótipo para esta função é
# def isNumberOrAlpha(char x):

import math


def readNumber(m):
    while -100 <= m <= 100:
        m = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= m <= 100:
            return m
            break
        else:
            print("Valor errado volte a tentar")


def read():
        m = input("Insira um numero ou uma letra: ")
        n = input("Insira um numero ou uma letra")

def Exit():
    print("Programa finalizado")


def Maior():
    if m > n:
        print("O maior valor é: ", m)
    else:
        print("O maior valor é: ", n)


def Menor():
    if m < n:
        print("O menor valor é: ", m)
    else:
        print("O menor valor é: ", n)


def Media():
    print("A mendia dos valores é: ", (m + n) / 2)


def sinais():
    if m < 0 and n < 0:
        print("Ambos os valores são negativos")
    elif m >= 0 and n >= 0:
        print("Ambos os valores são positivos")
    else:
        print("Os valores não possuem o mesmo sinal")


def somaModulos():
    soma = m + n
    if soma < 0:
        soma *= -1
    print("A soma dos valores com o modulo é: ", soma)


def triangulo():
    if m > 0 and n > 0:
        h = math.sqrt(m ** 2 + n ** 2)
        print(f"A hipotenusa do triangulo é: {h:.2f}")
    else:
        print("Não é possivel realizar esta operação pois um dos sinais é negativo")


def menu():
    print("1 - Mostar o valor maus alto.")
    print("2 - Mostrar o valor mais baixo.")
    print("3 - Mostrar a media dos valores.")
    print("4 - Mostrar se os vlores têm o mesmo sinal")
    print("5 - Mostrar a soma dos módulos dos dois números")
    print("6 - Mostrar a hipotenusa do triangulo")
    print("0 - Sair.")
    while True:
        op = int(input())
        match op:
            case 0:
                Exit()
                break
            case 1:
                m = readNumber()
                n = readNumber()
                Maior()
            case 2:
                readNumber()
                Menor()
            case 3:
                readNumber()
                Media()
            case 4:
                readNumber()
                sinais()
            case 5:
                readNumber()
                somaModulos()
            case 6:
                readNumber()
                triangulo()
            case _:
                print("Opção invalida")


menu()
