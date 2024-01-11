SalBase = {
    "A": 1500,
    "B": 1500,
    "C": 1500,
    "D": 1250,
    "E": 1000,
    "F": 1000 
}

Categ = input("Digite a categoria profissional: ").upper()
print(f'A categoria {Categ:2} aufere {SalBase.get(Categ):5} euros de salário base')