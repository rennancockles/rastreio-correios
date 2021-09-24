from typing import Optional

from pydantic import BaseModel

from .destino import Destino
from .oec import OEC
from .unidade import Unidade


class Evento(BaseModel):
    tipo: Optional[str]
    status: Optional[str]
    data: Optional[str]
    hora: Optional[str]
    criacao: Optional[str]
    descricao: Optional[str]
    prazoGuarda: Optional[str]
    diasUteis: Optional[str]
    detalhe: Optional[str]
    unidade: Optional[Unidade]
    unidadeDestino: Optional[Destino]
    detalheOEC: Optional[OEC]

    def __init__(self, **data):
        super().__init__(**data)

        if "destino" in data and len(data.get("destino", list())) > 0:
            self.unidadeDestino = Destino(**data.get("destino")[0])
