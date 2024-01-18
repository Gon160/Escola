while True:
    N = int(input("Diga um numéro entre 1 e 20: "))
    if 1 > N < 20:
        print("Volte a tentar")
    else:
        break

fatorial = 1
for i in range(1, N + 1):
    fatorial *= i

print(f"{N}! =", end=" ")
for i in range(N, 0, -1):
    print(i, end="")
    if i != 1:
        print("x", end="")
    else:
        print(" =", fatorial)