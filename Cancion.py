from cantante import Cantante
from timeUtils import convertir_minutosfloat
class Cancion:
    def __init__(self, nombre, duracion, favorita, estrellas,cantante: Cantante):
        self.nombre = nombre
        self.duracion = duracion
        self.favorita = favorita
        self.estrellas = estrellas
        self.cantante=cantante


    def mostrarCancion(self):
        print (f"{self.nombre}, {convertir_minutosfloat(self.duracion)}, Favorita: {self.favorita}, {self.estrellas} estrellas, Cantante: {self.cantante.getNombre()}")

    def modificarEstrellas(self, val):
        self.estrellas = val