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

Nomes, SAtual, SFuturo,MAtual ,MFuturo = [], [], [], [], []
Conta = 0

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
    MAtual[i] = MAtual[i] + SAtual[i]
    print(f'MFuturo:  {MAtual[i]}')

for i in range(0, Conta, 1):
    if SAtual[i] >= 0 and SAtual[i] <= 500:
        SFuturo[i] = SAtual[i] * 0.1
        MFuturo[i] = MFuturo[i-1] + SAtual[i]
        print(f'MFuturo:  {MFuturo[i]}')
    elif SAtual[i] >= 501 and SAtual[i] <= 800:
        SFuturo[i] = SAtual[i] * 0.05
        MFuturo[i] = MFuturo[i-1] + SAtual[i]
        print(f'MFuturo:  {MFuturo[i]}')
    else:
        SFuturo[i] = SAtual[i]
        MFuturo[i] = MFuturo[i-1] + SAtual[i]
        print(f'MFuturo:  {MFuturo[i]}')

#print("Nome", end="")
#for i in range(1, Conta+1, 1):
#    print(f'{Nome}')
#    for N in 4:
#        print()