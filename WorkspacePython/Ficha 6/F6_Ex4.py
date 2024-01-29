#Modifique o programa anterior de forma a que sejam mostradas no ecrã todas as letras
#desde A até à letra introduzida, inclusive, usando para isso uma função com o seguinte
#protótipo:
#def fromAtoINPUT(n)
#As letras mostradas devem ser todas maiúsculas independentemente da letra
#introduzida ser ou não maiúscula. Considere o seguinte exemplo de execução:
def readData():
    while True:
        x = str(input("Insira um caractere de A-Z: "))
        if len(x) == 1 and x.isalpha():
            return x.upper()
            break
        else:
            print("Carectere invalido volte a tentar")

def fromAtoINPUT(x):
    for i in range(65, ord(x)+1):
        print(chr(i).upper())

x =readData()
fromAtoINPUT(x)
