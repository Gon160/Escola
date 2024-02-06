def inserN():
    while True:
        N = int(input("Diga um número entre 100 e 200: "))
        if 100 <= N <= 200:
            return N
            break
        else:
            print("O número inserido n esta entre 100 e 200!")

x = inserN()
y = inserN()

if x > y:
    N = y
    y = x
    x = N

for i in range(x, y + 1):
    if i % 2 == 0 and i % 7 == 0:
        print(i)