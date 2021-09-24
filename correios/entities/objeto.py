from typing import List, Optional

from pydantic import BaseModel

from .evento import Evento


class Objeto(BaseModel):
    cepDestino: Optional[str]
    dataPostagem: Optional[str]
    eventos: List[Evento] = list()
    numero: Optional[str]
    categoria: Optional[str]
    sigla: Optional[str]
    nome: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)

        if "evento" in data and len(data.get("evento", list())) > 0:
            evento = data.get("evento")[0]
            self.cepDestino = evento.get("cepDestino")
            self.dataPostagem = evento.get("dataPostagem")

            for evento in data.get("evento", list()):
                self.eventos.append(Evento(**evento))
