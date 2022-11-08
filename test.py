import pytest

from juguetes import Pelota, Pieza, Baldecito, Tachito, Ninie, Curiose, Revoltose


@pytest.fixture(autouse=True)
def before_each():
    pytest.pelota = Pelota(radio=4)
    pytest.cubo = Pieza(volumen=4)
    pytest.cilindro = Pieza(volumen=3, color='rosa')
    pytest.baldecito = Baldecito(costo_fijo=5, piezas_iniciales=[pytest.cubo, pytest.cilindro])
    pytest.iniciales = [Pieza(volumen=6), Pieza(volumen=5), Pieza(volumen=4)]
    pytest.tachito = Tachito(costo_fijo=3, piezas_iniciales=pytest.iniciales)
    pytest.todos_los_juguetes = [pytest.pelota, pytest.baldecito, pytest.tachito]
    pytest.valentin = Ninie(edad_en_meses=10, juguetes=pytest.todos_los_juguetes)
    pytest.zoe = Curiose(edad_en_meses=20, juguetes=[pytest.pelota, pytest.baldecito])
    pytest.milena = Revoltose(edad_en_meses=15)


def test_costo_fabricacion_pelota():
    assert pytest.pelota.costo_fabricacion() == 24


def test_costo_fabricacion_baldecito():
    assert pytest.baldecito.costo_fabricacion() == 21


def test_costo_fabricacion_tachito():
    assert pytest.tachito.costo_fabricacion() == 39


def test_eficacia_pelota():
    assert pytest.pelota.eficacia() == 12


def test_eficacia_baldecito():
    assert pytest.baldecito.eficacia() == 6


def test_eficacia_tachito():
    assert pytest.tachito.eficacia() == 15


def test_precio_pelota():
    assert pytest.pelota.precio_venta() == 144


def test_precio_baldecito():
    assert pytest.baldecito.precio_venta() == 101


def test_precio_tachito():
    assert pytest.tachito.precio_venta() == 189


def test_tiempo_valentin_pelota():
    assert round(pytest.valentin.tiempo_de_entretenimiento(pytest.pelota), 2) == 13.2


def test_tiempo_zoe_pelota():
    assert round(pytest.zoe.tiempo_de_entretenimiento(pytest.pelota), 2) == 21.6


def test_tiempo_milena_pelota():
    assert round(pytest.milena.tiempo_de_entretenimiento(pytest.pelota), 2) == 6


def test_valentin_acepta_todo():
    assert all(pytest.valentin.acepta_juguete(juguete) for juguete in pytest.todos_los_juguetes)


def test_zoe_acepta_pelota_y_baldecito():
    assert [pytest.pelota, pytest.baldecito] == list(
        filter(lambda juguete: pytest.zoe.acepta_juguete(juguete), pytest.todos_los_juguetes))


def test_milena_acepta_solo_tachito():
    assert [pytest.tachito] == list(
        filter(lambda juguete: pytest.milena.acepta_juguete(juguete), pytest.todos_los_juguetes))


def test_valentin_dona_a_milena():
    pytest.valentin.donar_juguetes(pytest.milena)
    assert pytest.valentin.juguetes == [pytest.pelota, pytest.baldecito]
    assert pytest.milena.juguetes == [pytest.tachito]
