from typing import Optional

from .endereco import Endereco


class OEC(object):
    def __init__(self, *args, **kwargs):
        self.lista: str = kwargs.get("lista", "")
        self.longitude: str = kwargs.get("longitude", "")
        self.latitude: str = kwargs.get("latitude", "")
        self.carteiro: str = kwargs.get("carteiro", "")
        self.distrito: str = kwargs.get("distrito", "")
        self.unidade: str = kwargs.get("unidade", "")
        self.endereco: Optional[Endereco] = None

        if "endereco" in kwargs:
            self.endereco = Endereco(**kwargs.get("endereco", dict()))
