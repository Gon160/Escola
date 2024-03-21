import csv

class Empresa:
    def __init__(self, id, nome, numero_funcionarios, lucro):
        self.id = id
        self.nome = nome
        self.numero_funcionarios =numero_funcionarios
        self.lucro = lucro

empresas = []

with open('exercicio6.csv','r') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linha in leitor:
        emp = Empresa(linha[0], linha[1], linha[2], linha[3])
        empresas.append(emp)

for emp in empresas:
    print(emp.id, emp.nome, emp.numero_funcionarios, emp.lucro)