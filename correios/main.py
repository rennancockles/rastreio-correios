from typing import Optional

import requests

from correios import Objeto


class Correios:
    usuario: str
    senha: str
    base_url: str = "http://webservice.correios.com.br/service/rest/rastro/rastroMobile"

    def __init__(self, usuario: str, senha: str):
        self.usuario = usuario
        self.senha = senha

    def _post(self, body):
        r = requests.post(
            self.base_url, data=body, headers={"Content-Type": "application/xml"}
        )

        if r.status_code == 200:
            return r.json()

    def rastreio(self, codigo: str) -> Optional[Objeto]:
        body = f"""
        <rastroObjeto>
            <usuario>{self.usuario}</usuario>
            <senha>{self.senha}</senha>
            <tipo>L</tipo>
            <resultado>T</resultado>
            <objetos>{codigo}</objetos>
            <lingua>101</lingua>
            <token>QTXFMvu_Z-6XYezP3VbDsKBgSeljSqIysM9x</token>
        </rastroObjeto>
        """

        json_result = self._post(body)

        if result := json_result.get("objeto", list()):
            objeto = Objeto(**result[0])
            objeto.json = json_result
            return objeto

        return None

    def geraCodValido(self, cod: str):
        cod = cod.strip()

        if len(cod) < 12 or 13 < len(cod):
            return ""

        prefixo = cod[0:2]
        numero = cod[2:10]
        sufixo = cod[-2:]
        multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]

        if len(numero) < 8 and len(cod) == 12:
            diferenca = 8 - len(numero)
            zeros = "0" * diferenca
            numero = zeros + numero

        soma = sum(int(numero[i]) * multiplicadores[i] for i in range(8))
        resto = soma % 11

        if resto == 0:
            dv = "5"
        elif resto == 1:
            dv = "0"
        else:
            dv = str(11 - int(resto))

        codfinal = prefixo + numero + dv + sufixo

        return codfinal
