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
