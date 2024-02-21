from Feira import feira_class

livro_0 = feira_class("Cem Anos de Solidão, por Gabriel García Márquez")
livro_1 = feira_class("1984, George Orwell")
livro_2 = feira_class("O Apanhador no Campo de Centeio, J.D. Salinger")
livro_3 = feira_class("Harry Potter e a Pedra Filosofal, J.K. Rowling")

print("Bem-vindo! Livraria Gama tem algumas ofertas para você!")
comprador = input("Digite seu nome para começarmos: ")
print(f"{comprador} temos 10 livros que combinam com você:"
'''
[0] Cem Anos de Solidão, por Gabriel García Márquez
[1] 1984, George Orwell
[2] O Apanhador no Campo de Centeio, J.D. Salinger
[3] Harry Potter e a Pedra Filosofal, J.K. Rowling''')

selecao = int(input("Selecione o número do livro desejado: "))
lista_livro = [livro_0, livro_1, livro_2, livro_3]
opcao_selecionada = int(selecao)

for opcao in lista_livro:
    if opcao_selecionada >= 5:
        print("Esta opção não está incluída em nossos livros.")
        break
    if opcao_selecionada <= 4:
        print(f"{comprador} seu livro {lista_livro[opcao_selecionada].emprestimo}.")
        print("Volte sempre!")
        break