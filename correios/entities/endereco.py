class Endereco(object):
    def __init__(self, *args, **kwargs):
        self.codigo = kwargs.get("codigo", "")
        self.cep = kwargs.get("cep", "")
        self.logradouro = kwargs.get("logradouro", "")
        self.numero = kwargs.get("numero", "")
        self.localidade = kwargs.get("localidade", "")
        self.uf = kwargs.get("uf", "")
        self.bairro = kwargs.get("bairro", "")
        self.latitude = kwargs.get("latitude", "")
        self.longitude = kwargs.get("longitude", "")
