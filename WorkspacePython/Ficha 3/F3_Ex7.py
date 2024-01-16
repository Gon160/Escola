#Elabore um programa que imprima uma lista de pré-seleção dos candidatos admitidos ao
#concurso de provimento de uma vaga para determinado cargo de uma empresa. Os candidatos
#que não satisfazem um dos seguintes requisitos são eliminados:
#• Classificação final de estágio superior a 13 valores;
#• Ter conhecimentos de inglês;
#• Ter experiência profissional internacional.
#A lista deverá apresentar a percentagem de candidatos pré-selecionados.

Nomes, sit = [], []
Conta = 0
while True:
    Nome = str(input("Diga o nome do candidato (ZZZ para terminar): "))
    if Nome.upper() == "ZZZ":
        break
    Nomes.append(Nome)
    Conta += 1
    Nota = float(input("Diga a nota do estágio: "))
    Ingles = str(input("Fluente em ingles (S/N): "))
    Internacional = str(input("Carreira internacional (S/N): "))
    if Nota > 13:
        if Ingles.upper() == "S" or Ingles.upper() == "SIM":
            if Internacional.upper() == "S" or Internacional.upper() == "SIM":
                Obs = "Selecionado(a)"
                sit.append(Obs)
            else:
                Obs = "Eliminado(a)"
                sit.append(Obs)
        else:
            Obs = "Eliminado(a)"
            sit.append(Obs)
    else:
        Obs = "Eliminado(a)"
        sit.append(Obs)

print("\nNome\t\tObservação")
for i in range(Conta):
    print("{:12}{}".format(Nomes[i], sit[i]))