lista = []
for i in range(0, 100, 5):
    lista.append(i)
print(lista)

nova_lista = [(valor + 3) for valor in lista]
print(nova_lista)

for item in range(len(lista)):
    lista[item] += nova_lista[item]

print(lista)