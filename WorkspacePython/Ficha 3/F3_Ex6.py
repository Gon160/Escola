#1. Inicializar as massas salariais e o contador de funcionários
#2. Imprimir o cabeçalho da lista
#3. Ler o nome e o salario do primeiro funcionário
#4. Enquanto o nome do Funcionário não for a sentinela ZZZ que indica o fim dos dados
    #a. Contar mais um funcionário
    #b. Calcular o salário futuro deste funcionário
        #i. Determinar a percentagem de aumento
    #c. Atualizar as massas salariais
    #d. Imprimir o nome e o salário atual e o futuro deste funcionário
    #e. Ler o nome e o salário atual do próximo funcionário
#5. Imprimir as massas salariais se o contador de funcionário for maior do que zero

Nomes, SAtual, SFuturo, MAtual ,MFuturo = [], [], [], 0, 0
Conta, j = 0, 0

while True:
    Nome = str(input("Diga o nome do funcionário (ZZZ para terminar): "))
    if Nome.upper() == "ZZZ":
        break
    Nomes.append(Nome)
    Dinheiro = float(input("Diga o salário atual do funcionário: "))
    while Dinheiro < 0:
        if Dinheiro < 0:
            print("Salário invalido")
            print("O salário precisa ser 0 ou maior")
            Dinheiro = float(input("Diga o salário atual do funcionário: "))
        else:
            break
    SAtual.append(Dinheiro)
    Conta += 1

for i in range(0, Conta, 1):
    MAtual += SAtual[i]

for i in range(0, Conta, 1):
    if 0 < SAtual[i] <= 500:
        SFuturo.append(SAtual[i] + SAtual[i] * 0.1)
    elif 501 <= SAtual[i] <= 800:
        SFuturo.append(SAtual[i] + SAtual[i] * 0.05)
    else:
        SFuturo.append(SAtual[i])
    MFuturo += SFuturo[i]

print("Nomes\t\tSAtual\t\tSFuturo")
for i in range(Conta):
    print("{:5}{:14.2f}{:14.2f}".format(Nomes[i], SAtual[i], SFuturo[i]))

print("MAtual: {:.2f}".format(MAtual))
print("MFuturo: {:.2f}".format(MFuturo))