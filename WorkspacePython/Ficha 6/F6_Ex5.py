#Escreva um programa que peça ao utilizador dois números reais, m e n, entre -100 e
#100, inclusive. Faça a leitura e validação de cada número à vez, usando uma função com
#o protótipo incluído a seguir, e que deve pedir para o utilizador introduzir um número
#no intervalo pretendido e devolver o número lido, após a validação do intervalo:
#def readNumber()

#Depois, através de uma função com o protótipo
#def menu()
#deve mostrar o seguinte menu e devolver a opção (validada), que é um número inteiro,
#escolhida pelo utilizador:

#1 - Show the largest value.
#2 - Show the smallest value.
#3 - Show the average value.
#0 - End.

#Finalmente, as opções listadas no menu devem ser implementadas sob a forma de
#funções. Estas funções são invocadas de acordo com a escolha do utilizador. O programa
#deve ficar em ciclo até a opção 0 ser escolhida. Considere o seguinte exemplo de
#execução:

#Insert real number a (between -100 and 100): -120.5
#** NUMBER OUT OF RANGE. Try again! **
#Insert real number a (between -100 and 100): -3
#Insert real number a (between -100 and 100): 1

#1- Show the largest value.
#2- Show the smallest value.
#3- Show the average value.
#0- End.

#1
#The largest value is 1.

#1- Show the largest value.
#2- Show the smallest value.
#3- Show the average value.
#0- End.

#0
#Exiting.


def readNumber():
    while True:
        m = int(input("Insira um numero entre -100 e 100: "))
        if -100 <= m <= 100:
            return m
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
                    print("O maior valor é: ", m)
                else:
                    print("O maior valor é: ", n)
            case 2:
                if m < n:
                    print("O menor valor é: ", m)
                else:
                    print("O menor valor é: ", n)
            case 3:
                print("A mendia dos valores é: ", (m+n)/2)
            case 4:
                print("Programa finalizado")
                break
            case _:
                print("Opção invalida")


m = readNumber()
n = readNumber()
menu()
