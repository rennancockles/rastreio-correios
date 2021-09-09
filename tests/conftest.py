import pytest

from correios import Correios


@pytest.fixture()
def correios():
    return Correios()
