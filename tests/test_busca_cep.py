def test_busca_cep_previous_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757540BR", previous=5, next=0
    )

    assert objeto == "QC067757494BR"


def test_busca_cep_next_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757400BR", previous=0, next=9
    )

    assert objeto == "QC067757494BR"


def test_busca_cep_zero_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757490BR", previous=0, next=0
    )

    assert objeto == "QC067757494BR"


def test_busca_cep_zero_not_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757540BR", previous=0, next=0
    )

    assert objeto == ""


def test_busca_cep_previous_not_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757510BR", previous=1, next=0
    )

    assert objeto == ""


def test_busca_cep_next_not_found(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757470BR", previous=0, next=1
    )

    assert objeto == ""


def test_busca_cep_previous_negative(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757510BR", previous=-5, next=-5
    )

    assert objeto == ""


def test_busca_cep_next_negative(correios):
    objeto = correios.busca_por_cep(
        cep="28620000", start_cod="QC067757470BR", previous=-5, next=-5
    )

    assert objeto == ""
