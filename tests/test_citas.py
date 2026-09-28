import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# TODO 1: prueba para "contributivo" (10 %).
def test_contributivo_paga_10_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000


# TODO 2: prueba para "subsidiado" (0).
def test_subsidiado_no_paga():
    assert calcular_copago(100000, "subsidiado") == 0


# TODO 3: prueba de valores inválidos: pytest.raises(ValueError).
def test_valor_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "contributivo")


def test_tipo_afiliado_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(100000, "prepagada")


# Prueba extra: verifica el redondeo a 2 decimales (10 % de 12345 = 1234.5).
def test_redondeo_a_dos_decimales():
    assert calcular_copago(12345, "contributivo") == 1234.5
