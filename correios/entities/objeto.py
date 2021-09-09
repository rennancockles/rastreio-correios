from typing import List

from .evento import Evento


class Objeto(object):
    def __init__(self, *args, **kwargs):
        self.cepDestino = ""
        self.dataPostagem = ""
        self.eventos: List[Evento] = list()
        self.numero = kwargs.get("numero", "")
        self.categoria = kwargs.get("categoria", "")
        self.sigla = kwargs.get("sigla", "")
        self.nome = kwargs.get("nome", "")
        self.json = ""

        if "evento" in kwargs and len(kwargs.get("evento", list())) > 0:
            evento = kwargs.get("evento")[0]
            self.cepDestino = evento.get("cepDestino", "")
            self.dataPostagem = evento.get("dataPostagem", "")

            for evento in kwargs.get("evento", list()):
                self.eventos.append(Evento(**evento))
