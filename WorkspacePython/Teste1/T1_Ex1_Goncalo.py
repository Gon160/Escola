def leMatriz():
    Matriz = []
    for i in range(3):
        Linha = []
        for j in range(3):
            x = int(input("Diga um numero para a matriz: "))
            Linha.append(x)
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
    for i in range(3):
        linha_resultado = []
        for j in range(3):
            SMatriz = a[i][j] + b[i][j]
            linha_resultado.append(SMatriz)
        resultado.append(linha_resultado)
    return resultado

print("Primeira matriz: ")
MatrizA = leMatriz()
mostrarMatriz(MatrizA)
print("\nSegunda matriz: ")
MatrizB = leMatriz()
mostrarMatriz(MatrizB)
print("\nTransposta da matriz A: ")
MatrizTA = transpostaMatriz(MatrizA)
mostrarMatriz(MatrizTA)
print("\nSoma das matrizes: ")
MatrizC = somarMatrizes(MatrizTA, MatrizB)
mostrarMatriz(MatrizC)