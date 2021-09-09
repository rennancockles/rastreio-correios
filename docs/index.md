<p align="center">
  <a href="https://rastreio-correios.r3ck.com.br">
    <img src="https://rastreio-correios.r3ck.com.br/assets/img/caminhao-correios.png" alt="Rastreio Correios Logo" />
  </a>
</p>

<p align="center">
    <em>Rastreamento de pacotes dos Correios.</em>
</p>

<p align="center">
  <a href="https://github.com/rennancockles/rastreio-correios/actions?query=workflow%3ACheck%20&%20Test" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/rennancockles/rastreio-correios/Check%20&%20Test?label=Test" alt="Test">
  </a>
  <a href="https://github.com/rennancockles/rastreio-correios/actions?query=workflow%3APublish" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/rennancockles/rastreio-correios/Publish?label=Publish" alt="Publish">
  </a>
  <a href="https://codecov.io/gh/rennancockles/rastreio-correios" target="_blank">
      <img src="https://img.shields.io/codecov/c/github/rennancockles/rastreio-correios?color=%2334D058" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/rastreio-correios/" target="_blank">
      <img src="https://img.shields.io/pypi/v/rastreio-correios?color=blue" alt="Package version">
  </a>
</p>

---

**Documentação**: <a href="https://rastreio-correios.r3ck.com.br" target="_blank">https://rastreio-correios.r3ck.com.br</a>

**Código Fonte**: <a href="https://github.com/rennancockles/rastreio-correios" target="_blank">https://github.com/rennancockles/rastreio-correios</a>

---

Rastreio-Correios é uma biblioteca simples para rastreamento de pacotes dos correios.

## Requisitos

Uma versão recente do <a href="https://www.python.org/downloads/" class="external-link" target="_blank">Python</a> (3.8 ou superior).

## Instalação

<div class="termy">

```console
$ pip install rastreio-correios
---> 100%
Successfully installed rastreio-correios
```

</div>

## Examplo

Para mais exemplos veja a página de <a href="https://rastreio-correios.r3ck.com.br/funcionalidades/" class="external-link" target="_blank">funcionalidades</a> na documentação.


```Python
from correios import Correios


correios = Correios()

objeto = correios.rastreio(cod="PM123456789BR")

if objeto and objeto.eventos:
    print(objeto.eventos[0].descricao)
```

## Licença

Esse projeto é licenciado sobre os termos da licença MIT.