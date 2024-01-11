print("Diga o seu nome: ")
Nome = str(input())
print("Diga o seu salário base: ")
SBase = float(input())
print("Diga a comissão por carros vendidos")
C = float(input())
print("Diga a percentagem sobre o valor das vendas (%)")
P = float(input())
print("Diga o numero de carros vendidos")
NCarros = int(input())
print("Diga o valor das vendas")
VVendas = float(input())
P = (P/100)*VVendas
C = NCarros * C
Sal = SBase + C + P
print(f'Salário a processar para {Nome} -> {Sal}€')