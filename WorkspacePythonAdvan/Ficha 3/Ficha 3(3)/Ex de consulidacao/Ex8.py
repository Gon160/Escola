import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @staticmethod
    def transforma_para_pessoas(*args):
        pessoas=[]
        with open("exercicio7.json","rt") as arquivo:
            arquivo_lido=arquivo.read()
            dicionario = json.loads(arquivo_lido)
            for key in dicionario:
                pessoa = Pessoa(key,dicionario[key])
                pessoas.append(pessoa)
            return pessoas

pessoas = Pessoa.transforma_para_pessoas()

for pessoa in pessoas:
    print(pessoa.nome , pessoa.idade)