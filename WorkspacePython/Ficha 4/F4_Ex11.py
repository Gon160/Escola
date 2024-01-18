#Elabore um programa que, a partir dos jogadores inscritos no Porto e em Lisboa, forme
#equipas de dois jogadores para um torneio de xadrez. No caso de sobrar um jogador
#inscrito, convoca-se o jogador emérito Ricardo.
#Algoritmo:
#
# Criar uma lista com os jogadores inscritos no Porto e outra com os inscritos em
#Lisboa
# Colocar esta lista de inscritos para formar as equipas de jogadores
# Se a lista clonada tiver um número ímpar de jogadores, convocar Ricardo
# Formar as equipas de dois jogadores a partir da lista de clonados.

JogadoresP = []
JogadoresL = []

while True:
    Nome = str(input("Nome do Jogador do Porto(ZZZ para terminar): "))
    if Nome.upper() == "ZZZ":
        break
    JogadoresP.append(Nome)

while True:
    Nome = str(input("Nome do Jogador de Lisboa(ZZZ para terminar): "))
    if Nome.upper() == "ZZZ":
        break
    JogadoresL.append(Nome)

if len(JogadoresP) % 2 != 0 or len(JogadoresP) < len(JogadoresL):
    JogadoresP.append("Ricardo")

if len(JogadoresL) % 2 != 0 or len(JogadoresL) < len(JogadoresP):
    JogadoresL.append("Ricardo")

for i in range(0, len(JogadoresL)):
    print(f"Equipa {i+1} = ['{JogadoresP[i]}'], ['{JogadoresL[i]}']")
