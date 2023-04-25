import re

# https://rogerbank.com.br/cambio

url = "https://www.rogerbank.com/cambio"

padrao_url = re.compile('(http(s)?://)?(www.)?rogerbank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A URL não é válida')

print('A URL é válida')