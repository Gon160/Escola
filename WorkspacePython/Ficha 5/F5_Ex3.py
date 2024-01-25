# Em seguimento do exercício 1, elabore um programa que leia a opção escolhida por
# um cliente e a quantidade encomendada e calcule a respetiva despesa.

Menus = {
    1: {"Desc": "Café e bolo de arroz", "PU": 1.3},
    2: {"Desc": "Dois cafés e meia torrada", "PU": 2.2},
    3: {"Desc": "Meia de leite e tosta com manteiga", "PU": 3},
    4: {"Desc": "Galão com tosta mista", "PU": 3.5}
}

print("===============Menus Disponíveis===============")
for NMenu, Menu in Menus.items():
    print(f"{NMenu}. {Menu['Desc']:37} {Menu['PU']:.2f} €")
print()

#while True:
#    op = int(input("Escolha um dos menus (1, 2, 3, 4): "))
#    match op:
#        case 1:
#            Qnt = int(input("Quantos menus quer? "))
#            Total = Menus[op]['PU'] * Qnt
#            print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
#            break
#        case 2:
#            Qnt = int(input("Quantos menus quer? "))
#            Total = Menus[op]['PU'] * Qnt
#            print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
#            break
#        case 3:
#            Qnt = int(input("Quantos menus quer? "))
#            Total = Menus[op]['PU'] * Qnt
#            print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
#            break
#        case 4:
#            Qnt = int(input("Quantos menus quer? "))
#            Total = Menus[op]['PU'] * Qnt
#            print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
#            break
#        case _:
#            print("O menu inserido não existe volte a tentar.")

while True:
    op = int(input("Escolha um dos menus (1, 2, 3, 4): "))
    if op == 1 or op == 2 or op == 3 or op == 4:
        Qnt = int(input("Quantos menus quer? "))
        Total = Menus[op]['PU'] * Qnt
        match op:
            case 1:
                print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
                break
            case 2:
                print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
                break
            case 3:
                print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
                break
            case 4:
                print(f"{Qnt} menus {Menus[op]['Desc']} = {Total}€")
                break
    else:
        print("O menu inserido não existe volte a tentar.")


#while True:
#    op = int(input("Escolha um dos menus (1, 2, 3, 4): "))
#    if op == 1 or op == 2 or op == 3 or op == 4:
#        Qnt = int(input("Quantos menus quer? "))
#        Total = Menus[op]['PU'] * Qnt
#        break
#    else:
#        print("O menu inserido não existe volte a tentar.")
#print(f"{Qnt} menus {Menus[op]['Desc']} = {Total:.2f}€")
