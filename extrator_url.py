class Extrator_URL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.get_url_base()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        if not self.url.startswith("http"):
            raise ValueError("Página Inválida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        if not url_base.endswith("cambio"):
            raise ValueError("Caminho Inválido")
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

extrator_url = Extrator_URL("https://rogerbank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_quantidade = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)
