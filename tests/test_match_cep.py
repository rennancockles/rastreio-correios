def test_cep_match(correios):
    matches = correios.match_cep(
        cep='28620000',
        cod='QC067757494BR',
    )

    assert matches

def test_cep_not_match_wrong_digit(correios):
    matches = correios.match_cep(
        cep='28620000',
        cod='QC067757490BR',
    )

    assert not matches

def test_cep_not_match(correios):
    matches = correios.match_cep(
        cep='28620001',
        cod='QC067757494BR',
    )

    assert not matches

def test_cod_not_match(correios):
    matches = correios.match_cep(
        cep='28620000',
        cod='QC067757480BR',
    )

    assert not matches
