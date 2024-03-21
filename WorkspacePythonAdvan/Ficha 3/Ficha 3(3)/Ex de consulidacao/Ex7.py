import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @staticmethod
    def transforma_dict(*args):
        dicionario = dict()
        for pessoa in args:
            dicionario[pessoa.nome] = pessoa.idade
        return dicionario

pessoa1 = Pessoa("Carlos","45")
pessoa2 = Pessoa("Maria","67")
pessoa3 = Pessoa("Pedro","23")

dictionario_pessoas = Pessoa.transforma_dict(pessoa1,pessoa2,pessoa3)
texto = json.dumps(dictionario_pessoas, indent=4)
print(texto)
with open('exercicio7.json','wt') as arquivo:
    arquivo.write(texto)
