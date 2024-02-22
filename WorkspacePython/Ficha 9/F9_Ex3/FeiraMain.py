from Feira import feira_class

produto_0 = feira_class("Cem Anos de Solidão, por Gabriel García Márquez")
produto_1 = feira_class("1984, George Orwell")
produto_2 = feira_class("O Apanhador no Campo de Centeio, J.D. Salinger")
produto_3 = feira_class("Harry Potter e a Pedra Filosofal, J.K. Rowling")

print("Bem-vindo! A feira tem algumas ofertas para você!")
comprador = input("Digite seu nome para começarmos: ")
print(f"{comprador} temos 4 frutas para você:"
'''
[0] Maçã
[1] Banana
[2] Morango
[3] Ananás''')

selecao = int(input("Selecione o número da fruta desejada: "))
lista_produtos = [produto_0, produto_1, produto_2, produto_3]
opcao_selecionada = int(selecao)

for opcao in lista_produtos:
    if opcao_selecionada >= 5:
        print("Esta opção não está incluída em nossas frutas.")
        break
    if opcao_selecionada <= 4:
        print(f"{comprador} comprou: {lista_produtos[opcao_selecionada].nome_fruta}.")
        print("Volte sempre!")
        break