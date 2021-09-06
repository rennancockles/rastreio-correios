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
