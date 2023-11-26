class ListaCanciones:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.cantidad = 0
        self.duracion = '00:00'
        self.listaCancion = []

    def crearLista(self, lista):
        self.listaCancion.extend(lista)
        self.cantidad =self.cantidad+ len(lista)
        for cancion in lista:
            self.duracion = sumar_minutos(self.duracion, cancion.duracion)
    



    def sumar_minutos(min1, min2):
    # Convierte cada tiempo a segundos
    minutos1, segundos1 = map(int, min1.split(':'))
    minutos2, segundos2 = map(int, min2.split(':'))
    total_segundos1 = minutos1 * 60 + segundos1
    total_segundos2 = minutos2 * 60 + segundos2

    # Suma los segundos totales
    suma_total_segundos = total_segundos1 + total_segundos2

    # Convierte la suma total de nuevo a minutos y segundos
    minutos_totales = suma_total_segundos // 60
    segundos_totales = suma_total_segundos % 60

    return f"{minutos_totales}:{segundos_totales:02d}"

    def mostrarLista(self):
        return [cancion.mostrarCancion() for cancion in self.listaCancion]

    def ordenarLista(self):
        self.listaCancion.sort(key=lambda x: x.nombre)