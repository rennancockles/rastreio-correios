def test_gera_codigo_valido_1(correios):
    valid_cod = 'QC067757494BR'
    assert correios.gera_codigo_valido(cod='QC06775749BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC067757490BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC067757494BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC067757495BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC067757499BR') == valid_cod

def test_gera_codigo_valido_2(correios):
    valid_cod = 'PM892012097BR'
    assert correios.gera_codigo_valido(cod='PM89201209BR') == valid_cod
    assert correios.gera_codigo_valido(cod='PM892012090BR') == valid_cod
    assert correios.gera_codigo_valido(cod='PM892012096BR') == valid_cod
    assert correios.gera_codigo_valido(cod='PM892012097BR') == valid_cod
    assert correios.gera_codigo_valido(cod='PM892012099BR') == valid_cod

def test_gera_codigo_valido_3(correios):
    valid_cod = 'QC240005664BR'
    assert correios.gera_codigo_valido(cod='QC24000566BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC240005660BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC240005664BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC240005665BR') == valid_cod
    assert correios.gera_codigo_valido(cod='QC240005669BR') == valid_cod

def test_gera_codigo_valido_large_cod(correios):
    assert correios.gera_codigo_valido(cod='QC2400056644BR') == ""
    assert correios.gera_codigo_valido(cod='QC24000566444BR') == ""

def test_gera_codigo_valido_small_cod(correios):
    assert correios.gera_codigo_valido(cod='QC2400056BR') == "QC024000566BR"
    assert correios.gera_codigo_valido(cod='QC240005BR') == "QC002400054BR"

def test_gera_codigo_valido_no_letters(correios):
    assert correios.gera_codigo_valido(cod='240005665BR') == ""
    assert correios.gera_codigo_valido(cod='QC240005665') == ""
