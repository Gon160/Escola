import math

class EstudanteInf():
    def __init__ (self, N, T1, T2):
        self.Nome = N
        self.Teste1 = T1
        self.Teste2 = T2
    def ClassFinal(self):
        return math.floor((self.Teste1 + self.Teste2) / 2+0.5)

E=EstudanteInf('Ana Paiva', 14, 16)
print (f'{E.Nome } teve a classif. finai de {E.ClassFinal()} valores')
