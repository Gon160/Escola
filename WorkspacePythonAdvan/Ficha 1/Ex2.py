class AnoInvalidoException(Exception):
    pass

class MesInvalidoException(Exception):
    pass

class DiaInvalidoException(Exception):
    pass

def verificar_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    else:
        return False

def verificar_mes_dia(mes, dia):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia >= 1 and dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia >= 1 and dia <= 30
    elif mes == 2:
        return dia >= 1 and dia <= 29
    else:
        return False

try:

    mes = int(input("Digite o mês: "))
    if mes < 1 or mes > 12:
        raise MesInvalidoException("O mês é inválido")

    dia = int(input("Digite o dia: "))
    if not verificar_mes_dia(mes, dia):
        raise DiaInvalidoException("O dia é inválido para o mês insirido")

    ano = int(input("Digite o ano: "))
    if ano <= 1980 or ano >= 2030:
        raise AnoInvalidoException("O ano é inválido")

    if mes == 2 and not verificar_bissexto(ano) and dia == 29:
        raise DiaInvalidoException("Dia inválido para ano não bissexto")

    print(f"A data inserida foi: {dia}/{mes}/{ano}")

except ValueError:
    print("Por favor, insira valores numéricos para ano, mês e dia.")
except AnoInvalidoException as e:
    print(f"Ano inválido: {e}")
except MesInvalidoException as e:
    print(f"Mês inválido: {e}")
except DiaInvalidoException as e:
    print(f"Dia inválido: {e}")
finally:
    print(f"Valores inseridos: dia={dia} , mês={mes}, ano={ano}")
