from Curso import Curso
from Aluno import Aluno
from Professor import Professor

listaOpcoes = ["\n\n0-) Sair\n"
               "1-) Ver lista de alunos\n"
               "2-) Incluir um novo aluno\n"
               "3-) Excluir um aluno existente\n"
               "4-) Ver um aluno\n"
               "5-) Ver lista de professor\n"
               "6-) Incluir um novo professor\n"
               "7-) Excluir um professor existente\n"
               "8-) Ver um professor\n"
               "9-) Ver listar de curso\n"
               "10-) Incluir um novo curso\n"
               "11-) Excluir um curso existente\n"
               "12-) Ver um curso\n"]
listaProfessores = []
listaAlunos = []
listaCursos = []

while True:
    print(f"{listaOpcoes[0]}")
    Op = int(input("Digite a opção pretendida: "))
    if Op == 0:
        print(f"A sair do programa...")
        break
    elif Op == 1:
        for aluno in listaAlunos:
            print(f"Informações do aluno: {aluno.nome}\n"
                  f"Documento: {aluno.documento}\n"
                  f"Matricula: {aluno.matricula}")
    elif Op == 2:
        Nome = input("Digite o nome do aluno: ")
        Documento = input("Digite o documento do aluno: ")
        Matricula = input("Digite a matricula do aluno: ")
        listaAlunos.append(Aluno(Nome, Documento, Matricula))
    elif Op == 3:
        while True:
            contador = 0
            for aluno in listaAlunos:
                print(f"{aluno.nome, aluno.documento, aluno.matricula} - {contador}")
                contador += 1
            print(f"Se desistiu, digite {contador} para sair!")
            contadorSelecionado = int(input("Qual o número da informação deseja excluir: "))
            if contadorSelecionado in range(0, contador):
                print("Estamos excluindo... quase lá...")
                lista_selecionada = listaAlunos.pop(contadorSelecionado)
                print(f"As informações do aluno {lista_selecionada.nome} foram excluidas|")
                break
            elif contadorSelecionado == contador:
                break
            else:
                print("Informação não existe")
    elif Op == 4:
        print("Nome dos alunos: ")
        for aluno in listaAlunos:
            print(f"{aluno.nome}")
        nomeEscolhido = input("Digite o nome do aluno que pretende excluir: ")
        existente = 0
        for aluno in listaAlunos:
            if nomeEscolhido == aluno.nome:
                print(f"O aluno {aluno.nome} tem a matricula {aluno.matricula} e o documento {aluno.documento}")
                existente += 1
        if existente == 0:
            print(f"O aluno pretendido não existe")

    elif Op == 5:
        for professor in listaProfessores:
            print(f"Informações do professor: {professor.nome}\n"
                  f"Disciplina: {professor.disciplina}\n"
                  f"Matricula: {professor.matricula}")
    elif Op == 6:
        Nome = input("Digite o nome do professor: ")
        Disciplina = input("Digite a disciplina do professor: ")
        Matricula = input("Digite a matricula do professor: ")
        listaProfessores.append(Professor(Nome, Disciplina, Matricula))
    elif Op == 7:
        while True:
            contador = 0
            for professor in listaProfessores:
                print(f"{professor.nome, professor.disciplina, professor.matricula} - {contador}")
                contador += 1
            print(f"Se desistiu, digite {contador} para sair!")
            contadorSelecionado = int(input("Qual o número da informação deseja excluir: "))
            if contadorSelecionado in range(0, contador):
                print("Estamos excluindo... quase lá...")
                lista_selecionada = listaProfessores.pop(contadorSelecionado)
                print(f"As informações do professor {lista_selecionada.nome} foram excluidas|")
                break
            elif contadorSelecionado == contador:
                break
            else:
                print("Informação não existe")
    elif Op == 8:
        print("Nome dos professores: ")
        for professor in listaProfessores:
            print(f"{professor.nome}")
        nomeEscolhido = input("Digite o nome do professor que pretende excluir: ")
        existente = 0
        for professor in listaProfessores:
            if nomeEscolhido == professor.nome:
                print(
                    f"O professor {professor.nome} tem a matricula {professor.matricula} e ensina {professor.matricula}")
                existente += 1
        if existente == 0:
            print(f"O professor pretendido não existe")

    elif Op == 9:
        for curso in listaCursos:
            print(f"Informações do curso: {curso.nome}\n"
                  f"Periodo: {curso.periodo}\n")
    elif Op == 10:
        Nome = input("Digite o nome do aluno: ")
        Periodo = input("Digite o periodo: ")
        listaCursos.append(Curso(Nome, Periodo))
    elif Op == 11:
        while True:
            contador = 0
            for curso in listaCursos:
                print(f"{curso.nome, curso.periodo} - {contador}")
                contador += 1
            print(f"Se desistiu, digite {contador} para sair!")
            contadorSelecionado = int(input("Qual o número da informação deseja excluir: "))
            if contadorSelecionado in range(0, contador):
                print("Estamos excluindo... quase lá...")
                lista_selecionada = listaCursos.pop(contadorSelecionado)
                print(f"As informações do curso {lista_selecionada.nome} foram excluidas|")
                break
            elif contadorSelecionado == contador:
                break
            else:
                print("Informação não existe")
    elif Op == 12:
        print("Nome dos alunos: ")
        for curso in listaCursos:
            print(f"{curso.nome}")
        nomeEscolhido = input("Digite o nome do aluno que pretende excluir: ")
        existente = 0
        for curso in listaCursos:
            if nomeEscolhido == curso.nome:
                print(f"O curso {curso.nome} esta no {curso.periodo} periodo")
                existente += 1
        if existente == 0:
            print(f"O curso pretendido não existe")
