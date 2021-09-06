from .endereco import Endereco


class Unidade(object):
    def __init__(self, *args, **kwargs):
        self.local = kwargs.get("local", "")
        self.codigo = kwargs.get("codigo", "")
        self.cidade = kwargs.get("cidade", "")
        self.uf = kwargs.get("uf", "")
        self.sto = kwargs.get("sto", "")
        self.tipounidade = kwargs.get("tipounidade", "")

        if "endereco" in kwargs:
            self.endereco = Endereco(**kwargs.get("endereco", dict()))
