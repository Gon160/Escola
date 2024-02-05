# Escreva um programa que leia, do teclado, duas matrizes A e B, ambas com dimensões
# 2 x 3, compostas apenas por inteiros, e mostre:
#  a soma das matrizes, i.e., A + B;
#  o produto de A pela transposta de B, i.e., C = A x Transposta(B);
#  as coordenadas/índices dos valores negativos da matriz C.
#
# Os protótipos a usar nas funções a escrever são as que se incluem a seguir (note que
# algumas já foram desenvolvidas em exercícios anteriores e devem ser reutilizadas):
#  def inserirMatriz():
#  def mostrarMatriz(matriz):
#  def somarMatrizes(a,b):
#  def transpostaMatriz(matriz):
#  def multiplicaMatriz(a,b):
# sendo que matriz, a e b são matrizes bi-dimensionais (lista com listas dentro, em
# Python), e todas as funções devolvem um matriz (uma lista), exceto a última, que
# apenas imprime valores.
# Note que o produto de duas matrizes A e B, de dimensões p x q e q x p
# respetivamente, é uma nova matriz C de dimensões p x p em que o valor em cada
# posição (i, j) é dado por:
# C[i,j] = A[i,1] x B[1,j] + A[i,2] x B[2,j] + ... + A[i,q] x B[q,j].


def inserirMatriz():
    Matriz = []
    for i in range(2):
        Linha = []
        for j in range(3):
            while True:
                x = int(input("Diga um numero inteiro entre 0 a 9: "))
                if 0 <= x <= 9:
                    Linha.append(x)
                    break
                else:
                    print("Numero invalido!")
        Matriz.append(Linha)
    return Matriz


def mostrarMatriz(matriz):
    for Linha in matriz:
        for x in Linha:
            print(x, end=" ")
        print()


def transpostaMatriz(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        linha_transposta = []
        for j in range(len(matriz)):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)
    return transposta


def somarMatrizes(a, b):
    resultado = []
    for i in range(2):
        linha_resultado = []
        for j in range(3):
            SMatriz = a[i][j] + b[i][j]
            linha_resultado.append(SMatriz)
        resultado.append(linha_resultado)
    return resultado


def multiplicaMatriz(a, b):
#    for i in range(2):
#        for j in range(3):
#            C = sum(a[i][k] * b[j][k] for k in range(len(a[0])))
#            print(C, end=" ")
#        print()

    if len(a[0]) != len(b):
            print("Número de colunas de A deve ser igual ao número de linhas de B.")
            return None

    resultado = []
    transposta_B = transpostaMatriz(b)

    for i in range(len(a)):
        linha_resultado = []
        for j in range(len(transposta_B[0])):
            produto = sum(a[i][k] * transposta_B[j][k] for k in range(len(a[0])))
            linha_resultado.append(produto)
        resultado.append(linha_resultado)

    return resultado


print("Diga a primeira matriz: ")
MatrizA = inserirMatriz()
print()
print("Diga a segunda matriz: ")
MatrizB = inserirMatriz()
print("-------------------")
print("A matriz A")
mostrarMatriz(MatrizA)
print("A matriz B")
mostrarMatriz(MatrizB)
print("-------------------")
print("A transposta da matriz A")
mostrarMatriz(transpostaMatriz(MatrizA))
print("A transposta da matriz B")
mostrarMatriz(transpostaMatriz(MatrizB))
print("-------------------")
print("A soma das matrizes é: ")
mostrarMatriz(somarMatrizes(MatrizA, MatrizB))
print("-------------------")
print("A multiplicação das matrizes é: ")
mostrarMatriz(multiplicaMatriz(MatrizA, MatrizB))
