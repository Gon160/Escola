Alunos = {
    1: {"Nome": "Ana", "Idade": 17, "Aulas": 85},
    2: {"Nome": "Rui", "Idade": 18, "Aulas": 97},
    3: {"Nome": "Ema", "Idade": 19, "Aulas": 86},
    4: {"Nome": "Ivo", "Idade": 16, "Aulas": 100},
}
Sit = []
i = 0

for NAluno, Aluno in Alunos.items():
    if Aluno['Idade'] >= 18 and Aluno['Aulas'] < 90:
        Sit.append("Exluído por faltas")
    elif Aluno['Idade'] < 18 and Aluno['Aulas'] < 90:
        Sit.append("Recupera faltas")
    else:
        Sit.append("Aprovado")


print("Alunos\tNome\tIdade\tAulas(%)\tSituação")
for NAluno, Aluno in Alunos.items():
    print(f"{NAluno} \t{Aluno['Nome']} {Aluno['Idade']:6} {Aluno['Aulas']:7} \t\t{Sit[i]}")
    i += 1
