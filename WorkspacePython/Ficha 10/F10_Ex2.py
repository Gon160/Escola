valorCasa = float(input("Digite o valor da casa que pretende comprar: "))
saldo = float(input("Digite o valor do seu saldo: "))
anos = int(input("Em quantos anos pretende pagar: "))

verificar = saldo * 0.30
emprestimo = valorCasa - saldo

if emprestimo > verificar:
    prestacao = emprestimo / anos
    print("O seu empréstimo foi aprovado")
    print(f"O valor a ser emprestado é de {emprestimo:.2f}€ que sera dividido por {anos} anos o que dará um valor de {prestacao:.2f} por mês")
else:
    print("O seu empréstimo foi negado")