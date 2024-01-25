def readData():
    while True:
        x = str(input("Insira um caractere de A-Z: "))
        if len(x) == 1 and x.isalpha():
            return x
            break
        else:
            print("Carectere invalido volte a tentar")

def chanceCase(x):
    if x.islower():
        return x.upper()
    else:
        return x.lower()

x =readData()

print(f'O caractere inserido foi: {x}')
print(f'O caractere mudado é: {chanceCase(x)}')
