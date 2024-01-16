# Elabore um programa que imprima um retângulo, conhecendo a sua largura e o seu comprimento.
# Algoritmo
# 1. Desenhar linha do topo do retângulo, correspondente ao comprimento
# 2. Desenhar duas linhas verticais, uma em cada extremidade da linha do topo, para representarem a largura do retângulo
# 3. Desenhar a linha do fundo do retângulo, correspondente ao comprimento.

Comp = int(input('Digite o comprimento: '))
Larg = int(input('Digite o largura: '))

for l in range(1, Larg+1):
    print("X")
    for c in range(1, Comp+1):
        print("X", end="")
    print()