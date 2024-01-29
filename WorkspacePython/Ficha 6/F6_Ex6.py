# Escreva as seguintes funções para acrescentar funcionalidade ao programa anterior. Por
# cada função escrita, deve acrescentar a opção respetiva ao menu e correr o programa
# para verificar a sua correta implementação:
# • uma função que indique no ecrã se os números lidos têm sinal igual ou diferente;
# • uma função que mostre a soma dos módulos dos dois números;
# • uma função que mostre a hipotenusa dum triângulo retângulo se os valores lidos
# representarem os lados dos catetos (esta função só pode correr se os valores
# forem positivos; se não forem deve avisar e o programa deve voltar ao menu).

import math

def readNumber():
    while True:
        m = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= m <= 100:
            return m
            break
        else:
            print("Valor errado volte a tentar")


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
                Maior()
            case 2:
                Menor()
            case 3:
                Media()
            case 4:
                sinais()
            case 5:
                somaModulos()
            case 6:
                triangulo()
            case _:
                print("Opção invalida")


m = readNumber()
n = readNumber()
menu()