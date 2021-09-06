from .endereco import Endereco


class OEC(object):
    def __init__(self, *args, **kwargs):
        self.lista = kwargs.get('lista', '')
        self.longitude = kwargs.get('longitude', '')
        self.latitude = kwargs.get('latitude', '')
        self.carteiro = kwargs.get('carteiro', '')
        self.distrito = kwargs.get('distrito', '')
        self.unidade = kwargs.get('unidade', '')

        if 'endereco' in kwargs:
            self.endereco = Endereco(**kwargs.get('endereco', dict()))
