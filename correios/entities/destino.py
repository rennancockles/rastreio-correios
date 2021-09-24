from typing import Optional

from pydantic import BaseModel

from .endereco import Endereco


class Destino(BaseModel):
    bairro: Optional[str]
    local: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    codigo: Optional[str]
    endereco: Optional[Endereco]
