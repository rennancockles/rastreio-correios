from .destino import Destino
from .oec import OEC
from .unidade import Unidade


class Evento(object):
    def __init__(self, *args, **kwargs):
        self.tipo = kwargs.get('tipo', '')
        self.status = kwargs.get('status', '')
        self.data = kwargs.get('data', '')
        self.hora = kwargs.get('hora', '')
        self.criacao = kwargs.get('criacao', '')
        self.descricao = kwargs.get('descricao', '')
        self.prazoGuarda = kwargs.get('prazoGuarda', '')
        self.diasUteis = kwargs.get('diasUteis', '')
        self.detalhe = kwargs.get('detalhe', '')

        if 'unidade' in kwargs:
            self.unidade = Unidade(**kwargs.get('unidade', dict()))

        if 'destino' in kwargs and len(kwargs.get('destino', list())) > 0:
            self.destino = Destino(**kwargs.get('destino')[0])

        if 'detalheOEC' in kwargs:
            self.detalheOEC = OEC(**kwargs.get('detalheOEC', dict()))
