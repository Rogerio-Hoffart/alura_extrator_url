from functools import total_ordering
@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo
    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaSalario(37)
print(conta2 == conta1)
conta1.deposita(10)
print(conta2 == conta1)
conta3 = ContaSalario(21)
conta1.deposita(150)
conta2.deposita(80)
conta3.deposita(230)
contas = [conta1, conta2, conta3]

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

idades = [15, 17, 23, 43, 32, 65, 54, 32, 45]

for i in range(len(idades)):
    print(i, idades[i])

print(list(enumerate(idades)))

for indice, idade in enumerate(idades): #desempacotar tuppla
    print(indice, "x", idade)

print(sorted(idades))

print(list(reversed(sorted(idades))))

for conta in sorted(contas, reverse=True):
    print(conta)

conta4 = ContaSalario(12)
conta5 = ContaSalario(7)
conta6 = ContaSalario(4)

novas_contas = [conta4, conta5, conta6]

print(conta5 <= conta6)
print(conta5 <= conta4)