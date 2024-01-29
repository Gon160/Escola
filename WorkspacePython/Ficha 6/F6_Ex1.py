#Escreva um programa que peça ao utilizador um número inteiro n entre 1 e 100 inclusive
#(valide a entrada de dados). O programa deve mostrar no ecrã o resultado de:
#Sum(i=0)->(2 + i2) = (2+02) + (2+12) + (2+22) + ... + (2+n2)
#Este valor deve ser calculado numa função com o seguinte protótipo:
#def sum(n) que devolve o resultado pretendido.

def soma(x):
    valor = 0
    for i in range(x + 1):
        valor += x + i ** 2
    return valor


while True:
    x = int(input("Insira um número entre 1 e 100: "))
    if 1 <= x <= 100:
        break

print(f'Soma = {soma(x)}')
