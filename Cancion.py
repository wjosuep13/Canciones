from Cantante import Cantante
class Cancion:
    def __init__(self, nombre, duracion, favorita, estrellas,cantante: Cantante):
        self.nombre = nombre
        self.duracion = duracion
        self.favorita = favorita
        self.estrellas = estrellas
        self.cantante=cantante


    def mostrarCancion(self):
        return f"{self.nombre}, {self.duracion}, {self.favorita}, {self.estrellas} estrellas"

    def modificarEstrellas(self, val):
        self.estrellas = val