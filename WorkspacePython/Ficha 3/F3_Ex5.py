import math

Taxa = 2.5
Inicial = float(input("Capital inicial: "))
Meta, Acumu = Inicial * 1.2, 0
N = 0
while Acumu <= Meta:
    N += 1
    Acumu = Inicial * math.pow((1 + Taxa/100), N)
print(f'{Acumu:3.2f}€ ao fim de{N:2d} anos')    