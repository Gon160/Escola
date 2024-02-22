def contaSalarioL():

    valorIRS = IRS / 100
    valorIRS = SalarioI * valorIRS

    valorSS = SS / 100
    valorSS = SalarioI * valorSS

    salarioL = SalarioI - valorIRS - valorSS
    return salarioL

def contaSalarioLA():
    valorIRS = IRS / 100
    valorIRS = SalarioA * valorIRS

    valorSS = SS / 100
    valorSS = SalarioA * valorSS

    salarioL = SalarioA - valorIRS - valorSS
    return salarioL

SalarioI = float(input("Digite o seu salario atual: "))
IRS = float(input("Qual o valor q paga do IRS em precentagem: "))
SS = float(input("Qual o valor q paga da Segurança Social em precentagem: "))

print(f"Seu salario bruto atual é: {SalarioI:.2f}")
print(f"Seu salario liquido atual é: {contaSalarioL()}")

Aumento = float(input("Digite o valor do aumento: "))
SalarioA = SalarioI + (SalarioI * Aumento/100)

print(f"Seu salario bruto depois do seu aumento é: {SalarioA:.2f}")
print(f"Seu salario liquido depois do seu aumento é: {contaSalarioLA()}")

