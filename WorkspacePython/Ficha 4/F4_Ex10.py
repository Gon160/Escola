Jogadores = ["Ana", "Rui", "Telmo", "Beatriz", "Luisa", "Joana", "Manuel", "Pedro", "Paulo", "Paulino", "Maria", "Teresa"]

Contador = 0

while Contador < len(Jogadores):
    Equipa = Jogadores[Contador:Contador + 3]
    print(Equipa)
    Contador = Contador + 3
