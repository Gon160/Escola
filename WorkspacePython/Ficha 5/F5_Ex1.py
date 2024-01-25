Menus = {
    1: {"Desc": "Café e bolo de arroz", "PU": 1.3},
    2: {"Desc": "Dois cafés e meia torrada", "PU": 2.2},
    3: {"Desc": "Meia de leite e tosta com manteiga", "PU": 3},
    4: {"Desc": "Galão com tosta mista", "PU": 3.5}
}

for NMenu, Menu in Menus.items():
    print(f"{NMenu}. {Menu['Desc']} {Menu['PU']} €")
