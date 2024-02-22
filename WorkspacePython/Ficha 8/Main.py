from EstudanteInf import EstudanteInf

E = EstudanteInf("", 0, 0)
E.Nome = input("Digite o nome correto da aluna: ")
E.Teste1 = int(input(f"Digite a nota do teste 1 da aluna {E.Nome}: "))
E.Teste2 = int(input(f"Digite a nota do teste 2 da aluna {E.Nome}: "))
E.Impressao()
