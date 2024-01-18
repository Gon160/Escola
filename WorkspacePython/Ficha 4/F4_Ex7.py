while True:
    N = int(input("Diga um numero entre 1 e 10: "))
    if N < 1 or N > 10:
        print("Precisa de dizer um numero entre 1 e 10: ")
    else:
        break

print("Tabiado do ", N)
for i in range(1, 11):
    R = N*i
    print(f'{N} x {i} = {R}')
