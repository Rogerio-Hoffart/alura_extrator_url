from abc import ABCMeta, abstractmethod
import numpy as np

lista = []
for i in range(0, 100, 5):
    lista.append(i)
print(lista)

nova_lista = [(valor + 3) for valor in lista]
print(nova_lista)

for item in range(len(lista)):
    lista[item] += nova_lista[item]

print(lista)

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>codigo {} saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class Poupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
class Investimento(Conta):
    pass

def deposita_todas_contas(contas):
    for conta in contas:
        conta.deposita(100)

conta_do_roger = ContaCorrente(30)
print(conta_do_roger)
conta_do_roger.deposita(700)
print(conta_do_roger)
conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)
contas = [conta_dani, conta_do_roger]
print(contas)
for conta in contas:
    print(conta)
deposita_todas_contas(contas)
print(contas[0], contas[1])
contas1 = (conta_do_roger, conta_dani)
print(contas1)
for conta in contas1:
    print(conta)

deposita_todas_contas(contas)
for conta in contas1:
    print(conta)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = Poupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

novas_contas = [conta16, conta17]
for conta in novas_contas:
    conta.passa_o_mes()     #duck typing
    print(conta)

numeros = np.array([2.3, 3.76])
print(numeros)
numeros += 3
print(numeros)

conta43 = Investimento(43)