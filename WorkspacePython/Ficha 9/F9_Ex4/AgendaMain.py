from Agenda import agenda_class

listaAgenda = []

while True:
    print("[1] Adicionar pessoa\n"
          "[2] Remover pessoa\n"
          "[3] Mostrar agenda\n"
          "[4] Sair")
    op = int(input("Digite a opção desejada: "))

    if op == 1:
        nome = str(input("Digite o nome da pessoa: "))
        telefone = int(input("Digite o telefone da pessoa: "))
        endereco = str(input("Digite o endereço da pessoa: "))
        listaAgenda.append(agenda_class(nome, telefone, endereco))
    elif op == 2:
        while True:
            contador = 0
            for contato in listaAgenda:
                print(f"{contato.nome, contato.telefone, contato.endereco} - {contador}")
                contador += 1
            print(f"Se desistiu, digite {contador} para sair!")
            contadorSelecionado = int(input("Qual o número da informação deseja excluir: "))
            if contadorSelecionado in range(0, contador):
                print("Estamos excluindo... quase lá...")
                lista_selecionada = listaAgenda.pop(contadorSelecionado)
                print(f"O dado da agenda {lista_selecionada.nome, lista_selecionada.telefone, lista_selecionada.endereco} foi excluido|")
                break
            elif contadorSelecionado == contador:
                break
            else:
                print("Informação não existe")
    elif op == 3:
        print(f"Informações:")
        for i in listaAgenda:
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}")
