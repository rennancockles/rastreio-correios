from typing import Optional

from .endereco import Endereco


class Destino(object):
    def __init__(self, *args, **kwargs):
        self.bairro: str = kwargs.get("bairro", "")
        self.local: str = kwargs.get("local", "")
        self.cidade: str = kwargs.get("cidade", "")
        self.uf: str = kwargs.get("uf", "")
        self.codigo: str = kwargs.get("codigo", "")
        self.endereco: Optional[Endereco] = None

        if "endereco" in kwargs:
            self.endereco = Endereco(**kwargs.get("endereco", dict()))
