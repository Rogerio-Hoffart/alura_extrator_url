import re


class Extrator_URL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?rogerbank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def convercao(self, origem, valor):
        if origem == 'real':
            return (valor / 5.5)
        else:
            return (valor * 5.5)

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + f'Parãmetros: {self.get_url_parametros()}' + "\n" + f'URL base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url


url = "http://rogerbank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
extrator_url = Extrator_URL(url)
extrator_url2 = Extrator_URL(url)
print(f'O tamanho da URL: {len(extrator_url)}')
print(f'URL completa: {extrator_url}')
print(f'primeira URL é = a segunda? => {extrator_url == extrator_url2}')
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
print(f'A moeda de Origem será : {moeda_origem}')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
print(f'A moeda será convertida para: {moeda_destino}')
valor_quantidade = float(extrator_url.get_valor_parametro("quantidade"))
print(f'O valor a ser convertido é: {valor_quantidade}')

valor_convertido = round(extrator_url.convercao(moeda_origem, valor_quantidade), 2)

print(f' {valor_quantidade} unidades de {moeda_origem} equivalem a {valor_convertido} unidades de {moeda_destino}')

