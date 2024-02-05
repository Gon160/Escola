# Escreva um programa que leia uma matriz 2 x 3 só de números inteiros do teclado e
# mostre a matriz lida (A) e a sua transposta (B). Os protótipos a usar nas funções a
# escrever são os seguintes (algumas funções já foram desenvolvidas em exercícios
# anteriores e podem/devem ser reutilizadas):
#  def inserirMatriz():
#  def mostrarMatriz(matriz):
#  def transpostaMatriz(matriz):
# sendo que matriz é uma matriz bi-dimensional (lista com listas dentro, em Python),
# inserirMatriz() devolve a lista lida e transpostaMatriz(matriz) devolve a matriz (lista)
# transposta.
# Seja A uma matriz de dimensões p x q. A matriz transposta B = transposta(A) tem
# dimensões q x p e o valor em cada posição (i,j) é dado por B(i,j) = A(j,i). I.e., a matriz
# transposta troca os valores das linhas pelos das colunas e vice-versa.

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
    return Matriz()


def mostrarMatriz():

inserirMatriz()