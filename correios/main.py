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

    def gera_codigo_valido(self, cod: str):
        cod = cod.strip()

        if 13 < len(cod):
            return ""

        prefixo = cod[:2]
        sufixo = cod[-2:]
        numero = cod[2:-2][:8]
        multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]

        numero = self.format_num(numero)

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

    def match_cep(self, cep: str, cod: str) -> bool:
        if r := self.rastreio(cod):
            return r.cepDestino == cep
        return False

    def format_num(self, num: str) -> str:
        if len(num) < 8:
            diferenca = 8 - len(num)
            zeros = "0" * diferenca
            return zeros + num
        return num

    def busca_por_cep(
        self, cep: str, start_cod: str, previous: int = 0, next: int = 10
    ):
        cep = cep.replace("-", "")
        prefixo = start_cod[0:2]
        numero = int(start_cod[2:10])
        sufixo = start_cod[-2:]

        for p in range(previous):
            test_cod = self.gera_codigo_valido(f"{prefixo}{numero - (p + 1)}{sufixo}")
            if self.match_cep(cep, test_cod):
                return test_cod

        for n in range(next):
            test_cod = self.gera_codigo_valido(f"{prefixo}{numero + n}{sufixo}")
            if self.match_cep(cep, test_cod):
                return test_cod

        return ""
