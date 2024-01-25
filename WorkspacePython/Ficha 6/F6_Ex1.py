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
