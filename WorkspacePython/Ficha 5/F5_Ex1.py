# Determinada cafetaria tem os seguintes menus para pequenos-almoços:
# • Menu 1: café e bolo de arroz por 1.3 €;
# • Menu 2: dois cafés e meia torrada por 2.2 €;
# • Menu 3: Meia de leite e tosta com manteiga por 3€;
# • Menu 4: Galão com tosta mista por 3.5€
# Elabore um programa que crie um dicionário com a descrição (Desc) e o preço unitário
# (PU) de cada menu. A chave de cada entrada é o número de menu.

Menus = {
    1: {"Desc": "Café e bolo de arroz", "PU": 1.3},
    2: {"Desc": "Dois cafés e meia torrada", "PU": 2.2},
    3: {"Desc": "Meia de leite e tosta com manteiga", "PU": 3},
    4: {"Desc": "Galão com tosta mista", "PU": 3.5}
}

for NMenu, Menu in Menus.items():
    print(f"{NMenu}. {Menu['Desc']}, {Menu['PU']}€")