Desconto={
    "VEG": 0.15,
    "LAT": 0.10, 
    "CER": 0.10,
    "AGU": 0.10
}

CProd = input("Três primeiras letras da classe do produto: ").upper()
print(f'Os produtos da classe {CProd:3} têm {Desconto.get(CProd):2.0%} de desconto')