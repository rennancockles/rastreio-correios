from typing import Optional

from pydantic import BaseModel

from .endereco import Endereco


class Unidade(BaseModel):
    local: Optional[str]
    codigo: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    sto: Optional[str]
    tipounidade: Optional[str]
    endereco: Optional[Endereco]
