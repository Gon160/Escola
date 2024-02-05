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

m, n = None, None


def readNumber():
    global m
    global n
    while True:
        m = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= m <= 100:
            break
        else:
            print("Valor errado volte a tentar")

    while True:
        n = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= n <= 100:
            break
        else:
            print("Valor errado volte a tentar")

    return m, n


def read():
    global m
    global n
    m = str(input("Insira um numero ou uma letra: "))
    print("Oi eu sou o M: ", m)
    n = str(input("Insira um numero ou uma letra: "))
    print("Oi eu sou o N: ", n)
    return m, n

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
    soma = abs(m) + abs(n)
    print("A soma dos valores com o modulo é: ", soma)


def triangulo():
    if m > 0 and n > 0:
        h = math.sqrt(m ** 2 + n ** 2)
        print(f"A hipotenusa do triangulo é: {h:.2f}")
    else:
        print("Não é possivel realizar esta operação pois um dos sinais é negativo")


def isNumber():
    if 48 <= ord(m) <= 57:
        print("1")
    else:
        print("0")

    if 48 <= ord(n) <= 57:
        print("1")
    else:
        print("0")

def isAlpha():
    if 65 <= ord(m) <= 90 or 97 <= ord(m) <= 122:
        print("1")
    else:
        print("0")

    if 65 <= ord(n) <= 90 or 97 <= ord(n) <= 122:
        print("1")
    else:
        print("0")


def isNumberOrAlpha():
    if isNumber() or isAlpha():
        print("1")
    else:
        print("0")


def menu():
    print("1 - Mostar o valor maus alto.")
    print("2 - Mostrar o valor mais baixo.")
    print("3 - Mostrar a media dos valores.")
    print("4 - Mostrar se os vlores têm o mesmo sinal")
    print("5 - Mostrar a soma dos módulos dos dois números")
    print("6 - Mostrar a hipotenusa do triangulo")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("0 - Sair.")
    while True:
        op = int(input())
        match op:
            case 0:
                Exit()
                break
            case 1:
                readNumber()
                Maior()
                menu()
            case 2:
                readNumber()
                Menor()
                menu()
            case 3:
                readNumber()
                Media()
                menu()
            case 4:
                readNumber()
                sinais()
                menu()
            case 5:
                readNumber()
                somaModulos()
                menu()
            case 6:
                readNumber()
                triangulo()
                menu()
            case 7:
                read()
                isNumber()
                menu()
            case 8:
                read()
                isAlpha()
                menu()
            case 9:
                read()
                isNumberOrAlpha()
                menu()
            case _:
                print("Opção invalida")
        break


menu()
