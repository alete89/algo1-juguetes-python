class Juguete:
    CUV = 2

    def costo_fabricacion(self):
        pass

    def precio_venta(self):
        ef = self.eficacia()
        cf = self.costo_fabricacion()
        return ef * 10 + cf

    def eficacia(self):
        pass


class Pelota(Juguete):

    def __init__(self, radio):
        self.radio = radio

    def costo_fabricacion(self):
        return self.radio * 3 * Juguete.CUV

    def eficacia(self):
        return 12


class ConPiezas(Juguete):

    def __init__(self, costo_fijo, piezas_iniciales=None):
        self.costo_fijo = costo_fijo
        self.piezas = piezas_iniciales
        if piezas_iniciales is None:
            self.piezas = []

    def pieza_mayor_volumen(self):
        return max(self.piezas, key=lambda pieza: pieza.volumen)  # por suerte max acepta un 'key', sum, en cambio, no.
        # return max(pieza.volumen for pieza in self.piezas)  # pythonico usando generadores

    def costo_fabricacion(self):
        return self.costo_fijo + self.pieza_mayor_volumen().costo_fabricacion() * self.cantidad_piezas()

    def cantidad_piezas(self):
        return len(self.piezas)

    def hay_pieza_rosa(self):
        hay = any(pieza.es_rosa() for pieza in self.piezas)
        return hay

    def precio_venta(self):
        result = super().precio_venta() + (20 if self.hay_pieza_rosa() else 0)
        return result


class Baldecito(ConPiezas):
    minutos_fijos = 3

    def eficacia(self):
        return Baldecito.minutos_fijos * self.cantidad_piezas()


class Tachito(ConPiezas):

    def eficacia(self):
        return sum(pieza.eficacia() for pieza in self.piezas)  # pythonico, usa generadores en lugar de bloques/lambdas


class Pieza(Juguete):

    def __init__(self, volumen, color='azul'):
        self.volumen = volumen
        self.color = color

    def costo_fabricacion(self):
        return self.volumen * Juguete.CUV

    def eficacia(self):
        return self.volumen

    def es_rosa(self):
        return self.color == 'rosa'


class Ninie:

    def __init__(self, edad_en_meses, juguetes=None):
        self.edad_en_meses = edad_en_meses
        self.juguetes = juguetes
        if juguetes is None:
            self.juguetes = []

    def tiempo_de_entretenimiento(self, juguete):
        return juguete.eficacia() * self.coeficiente_entretenimiento()

    def coeficiente_entretenimiento(self):
        return 1 + self.edad_en_meses / 100

    def acepta_juguete(self, juguete):
        return True

    def recibir_juguete(self, juguete):
        self.juguetes.append(juguete)

    # def juguetes_que_acepta(self, juguetes):  # otro approach
    #     return list(filter(lambda juguete: self.acepta_juguete(juguete), juguetes))

    def donar_juguetes(self, otre):
        # for juguete in otre.juguetes_que_acepta(self.juguetes):
        for juguete in self.juguetes:
            if otre.acepta_juguete(juguete):
                otre.recibir_juguete(juguete)
                self.juguetes.remove(juguete)


class Curiose(Ninie):
    def tiempo_de_entretenimiento(self, juguete):
        return super().tiempo_de_entretenimiento(juguete) * 1.5

    def acepta_juguete(self, juguete):
        return juguete.precio_venta() < 150


class Revoltose(Ninie):
    def tiempo_de_entretenimiento(self, juguete):
        return juguete.eficacia() / 2

    def acepta_juguete(self, juguete):
        return self.tiempo_de_entretenimiento(juguete) > 7
