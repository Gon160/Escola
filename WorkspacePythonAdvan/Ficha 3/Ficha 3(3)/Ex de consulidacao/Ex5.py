import csv

def escreve_arquivo():
    with open('exercicio5.csv','w', newline='') as arquivo:
        escritorCSV = csv.writer(arquivo, delimiter=',')
        escritorCSV.writerow(['Nome','Parentesco'])
        escritorCSV.writerow(['Maria','Mãe'])
        escritorCSV.writerow(['Manuel','Pai'])
        escritorCSV.writerow(['Gonçalo','Filho'])

def le_arquivo():
    with open('exercicio5.csv','r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            print(linha)

escreve_arquivo()
le_arquivo()