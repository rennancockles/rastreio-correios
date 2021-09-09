from typing import Optional

from .endereco import Endereco


class Unidade(object):
    def __init__(self, *args, **kwargs):
        self.local: str = kwargs.get("local", "")
        self.codigo: str = kwargs.get("codigo", "")
        self.cidade: str = kwargs.get("cidade", "")
        self.uf: str = kwargs.get("uf", "")
        self.sto: str = kwargs.get("sto", "")
        self.tipounidade: str = kwargs.get("tipounidade", "")
        self.endereco: Optional[Endereco] = None

        if "endereco" in kwargs:
            self.endereco = Endereco(**kwargs.get("endereco", dict()))
