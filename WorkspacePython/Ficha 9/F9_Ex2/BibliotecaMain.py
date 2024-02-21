from Biblioteca import biblioteca_class

livro_0 = biblioteca_class("Cem Anos de Solidão, por Gabriel García Márquez")
livro_1 = biblioteca_class("1984, George Orwell")
livro_2 = biblioteca_class("O Apanhador no Campo de Centeio, J.D. Salinger")
livro_3 = biblioteca_class("Harry Potter e a Pedra Filosofal, J.K. Rowling")
livro_4 = biblioteca_class("Crime e Castigo, Fiódor Dostoiévski")
livro_5 = biblioteca_class("O Senhor dos Anéis, J.R.R. Tolkien")
livro_6 = biblioteca_class("Orgulho e Preconceito, Jane Austen")
livro_7 = biblioteca_class("A Metamorfose, Franz Kafka")
livro_8 = biblioteca_class("O Pequeno Príncipe, Antoine de Saint-Exupéry")
livro_9 = biblioteca_class("O Sol é para Todos, Harper Lee")

print("Bem-vindo! Livraria Gama tem algumas ofertas para você!")
comprador = input("Digite seu nome para começarmos: ")
print(f"{comprador} temos 10 livros que combinam com você:"
'''
[0] Cem Anos de Solidão, por Gabriel García Márquez
[1] 1984, George Orwell
[2] O Apanhador no Campo de Centeio, J.D. Salinger
[3] Harry Potter e a Pedra Filosofal, J.K. Rowling
[4] Crime e Castigo, Fiódor Dostoiévski
[5] O Senhor dos Anéis, J.R.R. Tolkien
[6] Orgulho e Preconceito, Jane Austen
[7] A Metamorfose, Franz Kafka
[8] O Pequeno Príncipe, Antoine de Saint-Exupéry
[9] O Sol é para Todos, Harper Lee''')

selecao = int(input("Selecione o número do livro desejado: "))
lista_livro = [livro_0, livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9]
opcao_selecionada = int(selecao)

for opcao in lista_livro:
    if opcao_selecionada >= 10:
        print("Esta opção não está incluída em nossos livros.")
        break
    if opcao_selecionada <= 9:
        print(f"{comprador} seu livro {lista_livro[opcao_selecionada].emprestimo}.")
        print("Volte sempre!")
        break