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
        if Ingles == "S":
            if Internacional == "S":
                Obs = "Selecionado"
                sit.append(Obs)
            else:
                Obs = "Eliminado"
                sit.append(Obs)
        else:
            Obs = "Eliminado"
            sit.append(Obs)
    else:
        Obs = "Eliminado"
        sit.append(Obs)