class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

produtos = []

with open('exercicio2.txt','rt') as arquivo:
    for linha in arquivo:
        indice_separa = linha.index("$")

        nome = linha[:indice_separa-1]
        valor = linha[indice_separa:len(linha)-1]
        produto = Produto(nome, valor)
        produtos.append(produto)

for produto in produtos:
    print(produto.nome, produto.valor)