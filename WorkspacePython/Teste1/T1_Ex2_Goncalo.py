Contador = 0
ContadorV = 0
while True:
    Frase = str(input("Escreva uma frase a seu gosto(a frase deve ter entre 20 a 100 caracteres e ponto final no fim): "))
    if len(Frase) >= 20 and len(Frase) <= 100:
        break
    else:
        print("A frase não possuem um número valido de caracteres!")

for i in Frase:
    if i == " " or i == ".":
        Contador += 1

for i in Frase:
    if i != "a" or i != "e" or i != "i" or i != "o" or i!= "u" or i != "A" or i != "E" or i != "I" or i != "O" or i!= "U":
        ContadorV += 1

print()
print(f'A frase é: {Frase}')
print(f'A frase tem {Contador} palavras')
print(f'A frase tem {ContadorV} letras sem as vogais')