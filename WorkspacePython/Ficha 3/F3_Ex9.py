#Elabore um programa que conte o número de palavras de uma frase. Por exemplo, a frase:
# “Até que as pedras se tornem mais leves que a água” tem 11 palavras.

#Algoritmo:
# 1. Atribuir a frase a uma variável
# 2. Inicializar o contador de palavras
# 3. Para cada carácter
#   a. Incrementar o contador de palavras se o caráter for um espaço ou um ponto final
# 4. Imprimir o contador de palavras
Contar = 0
while True:
    Frase = str(input("Diga uma frase: "))
    if Frase.upper() == "ZZZ":
        break
    for i in Frase:
        if i == " " or i == ".":
            Contar += 1
    print(f'A fraze "{Frase}" tem {Contar} palavras')
