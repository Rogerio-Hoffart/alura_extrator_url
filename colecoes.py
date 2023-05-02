
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