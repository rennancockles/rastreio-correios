from .endereco import Endereco


class Destino(object):
    def __init__(self, *args, **kwargs):
        self.bairro = kwargs.get("bairro", "")
        self.local = kwargs.get("local", "")
        self.cidade = kwargs.get("cidade", "")
        self.uf = kwargs.get("uf", "")
        self.codigo = kwargs.get("codigo", "")

        if "endereco" in kwargs:
            self.endereco = Endereco(**kwargs.get("endereco", dict()))
