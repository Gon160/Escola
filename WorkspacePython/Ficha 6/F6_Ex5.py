def readNumber():
    while True:
        m = int(input("Insira um numero entr e -100 e 100: "))
        if -100 <= m <= 100:
            return m
            break
        else:
            print("Valor errado volte a tentar")

    while True:
        n = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= n <= 100:
            return n
            break
        else:
            print("Valor errado volte a tentar")


def menu():
    print("1 - Mostar o valor maus alto.")
    print("2 - Mostrar o valor mais baixo.")
    print("3 - Mostrar a media dos valores.")
    print("0 - Sair.")
    while True:
        op = int(input())
        match op:
            case 1:
                if m > n:
                    print(m)
                else:
                    print(n)
            case 2:
                if m < n:
                    print(m)
                else:
                    print(n)
            case 3:
                print((m + n) / 2)
            case 4:
                print("Programa finalizado")
                break
            case _:
                print("Opção invalida")


m = readNumber()
n = readNumber()
menu()
