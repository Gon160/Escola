#Escreva um programa que peça ao utilizador um carater n que deverá corresponder a
#uma letra apenas (maiúscula ou minúscula). A leitura dos dados e respetiva validação
#devem ser feitas numa função que devolve o carater lido e com o seguinte protótipo:
#def readData()
#Se a letra introduzida é minúscula, o programa deve mostrar no ecrã a correspondente
#letra maiúscula e vice-versa. Deve usar, para esse efeito, uma função que aceita e
#devolve valores do tipo char, com o seguinte protótipo:
#def changeCase(n)
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
