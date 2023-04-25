endereco = "CEP 18077-412 Rua Antonio Menk, 130, Pq Laranjeiras, Sorocaba - SP "

import re #Regular Expression - ReGex

# CEP => 5 digitos + hífen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)  #Match

if busca:
    cep = busca.group()
    print(cep)