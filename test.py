from juguetes import Pelota, Pieza, Baldecito, Tachito, Ninie, Curiose, Revoltose


class TestJuguetes:
    pelota = Pelota(radio=4)
    cubo = Pieza(volumen=4)
    cilindro = Pieza(volumen=3, color='rosa')
    baldecito = Baldecito(costo_fijo=5, piezas_iniciales=[cubo, cilindro])
    iniciales = [Pieza(volumen=6), Pieza(volumen=5), Pieza(volumen=4)]
    tachito = Tachito(costo_fijo=3, piezas_iniciales=iniciales)
    todos_los_juguetes = [pelota, baldecito, tachito]
    valentin = Ninie(edad_en_meses=10, juguetes=todos_los_juguetes)
    zoe = Curiose(edad_en_meses=20, juguetes=[pelota, baldecito])
    milena = Revoltose(edad_en_meses=15)

    def test_costo_fabricacion_pelota(self):
        assert self.pelota.costo_fabricacion() == 24

    def test_costo_fabricacion_baldecito(self):
        assert self.baldecito.costo_fabricacion() == 21

    def test_costo_fabricacion_tachito(self):
        assert self.tachito.costo_fabricacion() == 39

    def test_eficacia_pelota(self):
        assert self.pelota.eficacia() == 12

    def test_eficacia_baldecito(self):
        assert self.baldecito.eficacia() == 6

    def test_eficacia_tachito(self):
        assert self.tachito.eficacia() == 15

    def test_precio_pelota(self):
        assert self.pelota.precio_venta() == 144

    def test_precio_baldecito(self):
        assert self.baldecito.precio_venta() == 101

    def test_precio_tachito(self):
        assert self.tachito.precio_venta() == 189

    def test_tiempo_valentin_pelota(self):
        assert round(self.valentin.tiempo_de_entretenimiento(self.pelota), 2) == 13.2

    def test_tiempo_zoe_pelota(self):
        assert round(self.zoe.tiempo_de_entretenimiento(self.pelota), 2) == 21.6

    def test_tiempo_milena_pelota(self):
        assert round(self.milena.tiempo_de_entretenimiento(self.pelota), 2) == 6

    def test_valentin_acepta_todo(self):
        assert all(self.valentin.acepta_juguete(juguete) for juguete in self.todos_los_juguetes)

    def test_zoe_acepta_pelota_y_baldecito(self):
        assert [self.pelota, self.baldecito] == list(
            filter(lambda juguete: self.zoe.acepta_juguete(juguete), self.todos_los_juguetes))

    def test_milena_acepta_solo_tachito(self):
        assert [self.tachito] == list(
            filter(lambda juguete: self.milena.acepta_juguete(juguete), self.todos_los_juguetes))

    def test_valentin_dona_a_milena(self):
        self.valentin.donar_juguetes(self.milena)
        assert self.valentin.juguetes == [self.pelota, self.baldecito]
        assert self.milena.juguetes == [self.tachito]
