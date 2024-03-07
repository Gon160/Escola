# Usa a função lambda para, fazer as contas da tabuada, por exemplo:
# tabuada2(5) que representa 2x5, ou tabuada6(3) que representa 6x3

def funcLambda(y):
    return lambda x: x * y


Tab1 = funcLambda(1)
Tab2 = funcLambda(2)
Tab3 = funcLambda(3)
Tab4 = funcLambda(4)
Tab5 = funcLambda(5)
Tab6 = funcLambda(6)
Tab7 = funcLambda(7)
Tab8 = funcLambda(8)
Tab9 = funcLambda(9)
Tab10 = funcLambda(10)

op = int(input("Indique a tabuada pretendida(1 - 10): "))
y = int(input("Qual o numero q pretende multiplicar: "))

match op:
    case 1:
        print(Tab1(y))
    case 2:
        print(Tab2(y))
    case 3:
        print(Tab3(y))
    case 4:
        print(Tab4(y))
    case 5:
        print(Tab5(y))
    case 6:
        print(Tab6(y))
    case 7:
        print(Tab7(y))
    case 8:
        print(Tab8(y))
    case 9:
        print(Tab9(y))
    case 10:
        print(Tab10(y))
    case _:
        print("opção invalida!")