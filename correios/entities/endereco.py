from typing import Optional

from pydantic import BaseModel


class Endereco(BaseModel):
    codigo: Optional[str]
    cep: Optional[str]
    logradouro: Optional[str]
    numero: Optional[str]
    localidade: Optional[str]
    uf: Optional[str]
    bairro: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
