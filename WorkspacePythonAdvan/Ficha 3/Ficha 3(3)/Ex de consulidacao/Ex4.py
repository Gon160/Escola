with open('exercicio4.txt','wt') as arquivo:
    for i in range(0,101):
        if i%3 == 0:
            arquivo.write(str(i) + '\n')