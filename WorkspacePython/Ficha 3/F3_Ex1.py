A = float(input("Diga o primeiro número"))
B = float(input("Diga o segundo número"))
C = float(input("Diga o terceiro número"))

if A<B:
    if A<C:
        Menor = A
    else:
        Menor = C
elif B<C:
    Menor = B
else: Menor = C
print(f'{Menor:3.2f} é o menor de {A:3.2f}, {B:3.2f} e {C:3.2f}')