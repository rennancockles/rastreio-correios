def test_rastreio_error(correios):
    objeto = correios.rastreio(cod="QC067757490BR")

    assert objeto
    assert objeto.numero == "QC067757490BR"
    assert objeto.categoria.startswith("ERRO:")


def test_rastreio_invalid(correios):
    objeto = correios.rastreio(cod="</objeto>QC067757490BR")
    assert not objeto


def test_rastreio_success(correios):
    objeto = correios.rastreio(cod="QC067757494BR")

    assert objeto
    assert objeto.numero == "QC067757494BR"
    assert objeto.sigla == "QC"
    assert objeto.cepDestino == "28620000"
    assert objeto.dataPostagem == "18/08/2021"
    assert objeto.eventos
