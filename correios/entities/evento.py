from typing import Optional

from .destino import Destino
from .oec import OEC
from .unidade import Unidade


class Evento(object):
    def __init__(self, *args, **kwargs):
        self.tipo: str = kwargs.get("tipo", "")
        self.status: str = kwargs.get("status", "")
        self.data: str = kwargs.get("data", "")
        self.hora: str = kwargs.get("hora", "")
        self.criacao: str = kwargs.get("criacao", "")
        self.descricao: str = kwargs.get("descricao", "")
        self.prazoGuarda: str = kwargs.get("prazoGuarda", "")
        self.diasUteis: str = kwargs.get("diasUteis", "")
        self.detalhe: str = kwargs.get("detalhe", "")
        self.unidade: Optional[Unidade] = None
        self.destino: Optional[Destino] = None
        self.detalheOEC: Optional[OEC] = None

        if "unidade" in kwargs:
            self.unidade = Unidade(**kwargs.get("unidade", dict()))

        if "destino" in kwargs and len(kwargs.get("destino", list())) > 0:
            self.destino = Destino(**kwargs.get("destino")[0])

        if "detalheOEC" in kwargs:
            self.detalheOEC = OEC(**kwargs.get("detalheOEC", dict()))
