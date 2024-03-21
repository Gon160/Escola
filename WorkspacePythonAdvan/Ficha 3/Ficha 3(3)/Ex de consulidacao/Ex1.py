lista = []
with open('exercicio1.txt','rt') as arquivo:
    for linha in arquivo:
        lista.append(linha)

    print(f'{lista}')