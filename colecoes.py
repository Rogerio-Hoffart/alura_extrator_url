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

texto1 = '''Testes de ponta a ponta são uma parte importante do processo de desenvolvimento de software. Eles permitem 
testar todo o fluxo da aplicação, desde a interação com o usuário até a persistência dos dados no banco de dados.
Neste artigo, eu separei algumas dicas essenciais que irão te ajudar muito a escrever testes de ponta a ponta melhores.
Antes de começar a escrever testes, é importante planejar o que será testado e como. Isso inclui identificar as 
funcionalidades e fluxos de usuário mais importantes, além de criar cenários que abranjam todas as etapas necessárias 
para a execução de uma ação. Com um planejamento adequado, é mais fácil garantir que os testes cubram todas as partes 
importantes da aplicação.
Um dos principais princípios dos testes de ponta a ponta é que eles devem ser independentes uns dos outros. Isso 
significa que cada teste deve ser executado em um ambiente isolado, sem depender do estado de outros testes. Para 
alcançar esse objetivo, você deve se certificar de que seus testes não compartilhem dados entre si, por exemplo, por 
meio de variáveis globais ou dados armazenados no banco de dados.'''

texto2 = '''Hoje vamos conversar sobre um termo que aparece muitas vezes quando se discute produtos de software:
 “quando você está criando uma classe, tem que pensar nas regras de negócio”, “ao planejar testes, sempre temos que 
 pensar nas regras de negócio”, “como estruturar um projeto? Vai depender das regras de negócio” e por aí vai.
As tais “regras de negócio” parecem muito importantes no desenvolvimento de software, mas nem sempre os conteúdos 
voltados a programação param para explicar este mistério: o que são, afinal, as regras de negócio e como elas se 
relacionam com o código?
Neste artigo vamos abordar as regras de negócio na visão do desenvolvimento de software, sem detalhar as partes que 
envolvem as pessoas de produto e stakeholders na criação destas regras. Lembrando sempre que a construção de um produto 
envolve diversas competências e que o código em si é uma parte disso!
O trabalho de desenvolvimento de software está ligado a, claro, escrever código. Mas o mais importante não é apenas 
saber como escrever, mas também o que escrever e por que escrever. É aí que entra a importância de se conhecer o produto
 ou serviço: o que faz, qual problema visa resolver e para quem.
Por exemplo, um time de desenvolvimento de um serviço voltado para a indústria alimentícia pode se envolver com diversos
aspectos que vão além do código, em assuntos como legislação sanitária para transporte de perecíveis, tributação de 
alimentos e por aí vai. É possível pensar em listas enormes de especificidades para cada app que você tem instalado no 
seu celular!
Ou seja, é imprescindível que devs conheçam e se envolvam com o produto, e isso passa pelas regras de negócio.'''

from collections import Counter

def analisa_freq_letras(texto):
    freq_caracteres = Counter(texto.lower())
    total_caracteres = sum(freq_caracteres.values())
    lista_letras = [(letra, frequencia/total_caracteres) for letra, frequencia in freq_caracteres.items()]
    lista_letras = Counter(dict(lista_letras))
    mais_comuns = lista_letras.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))

analisa_freq_letras(texto1)
analisa_freq_letras(texto2)
analisa_freq_letras(texto)


