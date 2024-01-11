nome, local, idade = "Gonçalo Gomes", "Covilhã", 16
print()
print(nome, local, idade)
print()
print(f'Olá eu sou o {nome} sou da {local} e tenho {idade} anos')

if __name__ == "__main__":
    mensagem="Fazer um if"
print (f'{mensagem}'.rjust(50))
print (f'{mensagem}'.center(50))
print (f'{mensagem}'.ljust(50))
print()
print (f"{mensagem:>50}")
print (f"{mensagem:^50}")
print (f"{mensagem:<50}")