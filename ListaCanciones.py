from tabulate import tabulate
from timeUtils import convertir_minutosfloat


class ListaCanciones:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.cantidad = 0
        self.duracion = 0.0
        self.listaCancion = []

    
    def crearLista(self, lista):
        self.listaCancion.extend(lista)
        self.cantidad =self.cantidad+ len(lista)
        for cancion in lista:
                self.duracion = self.duracion + cancion.duracion
    
    def mostrarLista(self):
        if not self.listaCancion:
            print("La lista está vacía.")
            return
        canciones_datos = [
            {
                'Canción': cancion.nombre,
                'Cantante': cancion.cantante.nombre,
                'Duración': convertir_minutosfloat(cancion.duracion),
                'Estrellas': cancion.estrellas,
                'Favorita': cancion.favorita

            }
            for cancion in self.listaCancion
        ]

        # Imprimir la lista tabulada
        print(tabulate(canciones_datos, headers="keys", tablefmt="grid",showindex=False))

    def ordenarLista(self, atributo):
        # Verifica si es un atributo anidado
        if "." in atributo:
            partes = atributo.split(".")
            self.listaCancion.sort(key=lambda cancion: getattr(getattr(cancion, partes[0]), partes[1]))
        else:
            # Si el atributo necesita una comparación numérica
            if atributo == 'duracion':
                self.listaCancion.sort(key=lambda cancion: float(cancion.duracion))
            elif atributo == 'estrellas':
                self.listaCancion.sort(key=lambda cancion: int(cancion.estrellas))
            # Ordena por el atributo directamente si no es un atributo anidado y no necesita conversión
            else:
                self.listaCancion.sort(key=lambda cancion: getattr(cancion, atributo))


