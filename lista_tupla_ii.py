class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

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

idades = [15, 17, 23, 43, 32, 65, 54, 32, 45]

for i in range(len(idades)):
    print(i, idades[i])

print(list(enumerate(idades)))

for indice, idade in enumerate(idades): #desempacotar tuppla
    print(indice, "x", idade)

print(sorted(idades))

print(list(reversed(sorted(idades))))