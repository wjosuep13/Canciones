class Cantante:
    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo = grupo

    def getNombre(self):
        return self.nombre

    def getGrupo(self):
        return self.grupo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setGrupo(self, grupo):
        self.grupo = grupo