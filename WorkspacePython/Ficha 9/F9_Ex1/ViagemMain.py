from Viagem import viagem_class

viagem_0 = viagem_class("Flórida")
viagem_1 = viagem_class("Havaí")
viagem_2 = viagem_class("Tóquio")
viagem_3 = viagem_class("Egito")
viagem_4 = viagem_class("Londres")
print("Bem-vindo! Viagens Gama tem algumas ofertas para você!")
viajante = input("Digite seu nome para começarmos: ")
print(f"{viajante} temos 5 destinos que combinam com você:"
'''
[0] Flórida
[1] Havaí
[2] Tóquio
[3] Egito
[4] Londres''')
#solicita ao utilizador a escolha da viagem
selecao = int(input("Selecione o número da viagem desejada: "))
#lista dos índices dos objetos para escolha
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4]
opcao_selecionada = int(selecao)
for opcao in lista_viagem:
    #caso o utilizador não escolha a opção correta
    if opcao_selecionada >= 5:
        print("Esta opção não está incluída em nossos destinos.")
        break
    #verifica a seleção
    if opcao_selecionada <= 4:
        #resultado
        print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} está marcada.")
        print("Volte sempre!")
        break