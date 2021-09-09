class Endereco(object):
    def __init__(self, *args, **kwargs):
        self.codigo: str = kwargs.get("codigo", "")
        self.cep: str = kwargs.get("cep", "")
        self.logradouro: str = kwargs.get("logradouro", "")
        self.numero: str = kwargs.get("numero", "")
        self.localidade: str = kwargs.get("localidade", "")
        self.uf: str = kwargs.get("uf", "")
        self.bairro: str = kwargs.get("bairro", "")
        self.latitude: str = kwargs.get("latitude", "")
        self.longitude: str = kwargs.get("longitude", "")
