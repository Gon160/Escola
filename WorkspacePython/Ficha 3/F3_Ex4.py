import math

Anos, AnoInicio = 3, 2024
Inicial, Acumu = 1500, 0
Taxa = (2, 2.5, 3)
Esp = " "*2

print(f'{Inicial:5d} €', end="")
for i in Taxa:
    print(f'{Esp}{i/100:^11.1%}', end="")
print()
for N in range(1, Anos+1, 1):
    print(f'{AnoInicio+N:5d}', end="")
    for i in Taxa:
        Acumu=Inicial*math.pow((1+i/100), N)
        print(f'{Acumu:13.2f}', end="")
    print()