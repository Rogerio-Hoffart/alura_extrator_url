with open("texto_manuseio.txt", "r", encoding='utf-8') as newt:
    texto = newt.readlines()
    texto = ''.join(texto).lower()
    palavras = {}

    for linha in texto.split():
        #palavras.append(linha.strip())
        #for letra in linha:
        palavras[linha] = palavras.get(linha, 0) + 1

#texto.close()
#palavras = ' '.join(palavras)
print(type(palavras))
print(palavras)


usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)
print(set(assistiram))
print(set(usuarios_data_science) | set(usuarios_machine_learning)) #União cjto
print(set(usuarios_data_science) & set(usuarios_machine_learning)) #Intersecção cjto
print(set(usuarios_data_science) - set(usuarios_machine_learning)) #Subtraçao cjto

usuarios = {1,5,76,34,52,13}
usuarios.add(17)
print(usuarios)
usuarios = frozenset(usuarios)
print(type(usuarios))
meu_texto = "Este texto é um teste para gerar um conjunto de palavras e testarmos a diferença entre lista e conjunto"
print(set(meu_texto.split()))

aparicoes = {"texto":1, "entre":2, "para":5, "lista":3}
print(aparicoes)
for item in aparicoes:
    print(f'Palavra - {item} e quantidade {aparicoes[item]}')
aparicoes["Carlos"] = 2
print(aparicoes)
del aparicoes["entre"]
print(aparicoes)
for item in aparicoes.values():
    print(item)
for item in aparicoes.items():
    print(item)
for chave, valor in aparicoes.items():
    print(chave, "=", valor)
print(["esta é a palavra {}".format(chave) for chave in aparicoes.keys()])
print(aparicoes.get("Carlos"))

novas_aparicoes = {}
for palavra in texto.split():
    ate_agora = novas_aparicoes.get(palavra, 0)
    novas_aparicoes[palavra] = ate_agora + 1

print(novas_aparicoes)

nome = 'Rogerio'
iteravel = iter(nome)

while True:
    try:
        print(next(iteravel))
    except StopIteration:
        break




