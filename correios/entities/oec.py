from typing import Optional

from pydantic import BaseModel

from .endereco import Endereco


class OEC(BaseModel):
    lista: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]
    carteiro: Optional[str]
    distrito: Optional[str]
    unidade: Optional[str]
    endereco: Optional[Endereco]
