#librerias
import csv

#utilidades
from timeUtils import convertir_minutosfloat
#clases propias
from cantante import Cantante
from cancion import Cancion
from listaCanciones import ListaCanciones
#lista global donde estarán las listas de canciones
listadoListas = []

def print_error(message):
    print("\n\033[91m\033[1mERROR:\033[0m", message, "\n")

def loadData():
    lista = []
    filename = 'canciones.csv'
    try:
        print(f"Cargando datos desde {filename}...")
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_dict_reader = csv.DictReader(file)
            for row in csv_dict_reader:
                try:
                    cancion = row['Cancion']
                    cantante = row['Cantante']
                    duracionstr = row['Duracion']
                    estrellas = row['Estrellas']
                    grupo = row['Grupo']
                    favorita = row['Favorita']
                    cantante = Cantante(cantante, grupo)
                    duracion = float(duracionstr.replace(" ", ""))
                    cancion = Cancion(cancion, duracion, favorita, estrellas, cantante)
                    cancion.mostrarCancion()
                    lista.append(cancion)
                except KeyError as e:
                    print_error(f"Falta un campo esperado en el archivo CSV: {e}")
                except ValueError:
                    print_error(f"Error al convertir datos para la canción: {cancion}. Revisar duración y estrellas.")
    except FileNotFoundError:
        print_error(f"El archivo {filename} no se encontró.")
    except Exception as e:
        print_error(f"Ocurrió un error al cargar los datos: {e}")

    return lista
    
def ingresar_entero(mensaje, rango=None):
    while True:
        try:
            valor = int(input(mensaje))
            if rango:
                # Verifica si el rango tiene un límite superior
                if rango[1] is None:
                    # Si solo hay un límite inferior
                    if valor < rango[0]:
                        print_error(f"Por favor, ingrese un número mayor o igual a {rango[0]}.")
                        continue
                else:
                    # Si hay un límite inferior y superior
                    if not rango[0] <= valor <= rango[1]:
                        print_error(f"Por favor, ingrese un número entre {rango[0]} y {rango[1]}.")
                        continue
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def ingresar_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor <= minimo:
                print_error(f"Por favor, ingrese un número mayor que {minimo}.")
                continue
            return valor
        except ValueError:
            print_error("Por favor, ingrese un número válido.")

def ingresar_cadena(mensaje, permitidos=None):
    while True:
        cadena = input(mensaje)
        if permitidos and cadena.lower() not in permitidos:
            print_error(f"Por favor, ingrese uno de los siguientes valores: {', '.join(permitidos)}")
            continue
        return cadena.lower()

def ingresarCancionesaLista():
    cantidad = ingresar_entero("Ingrese la cantidad de canciones a agregar: ", rango=(1, None))
    lista = []
    for i in range(cantidad):
        print(f"Ingrese los datos de la canción {i + 1}:")
        nombre = input("Ingrese el nombre de la canción: ")
        duracion = ingresar_flotante("Ingrese la duración de la canción (minutos): ", minimo=0)
        favorita = ingresar_cadena("¿La canción es favorita? (sí/no): ", permitidos=["sí", "si", "no"])
        estrellas = ingresar_entero("Ingrese la cantidad de estrellas (1-5): ", rango=(1, 5))
        print("Ingrese los datos del cantante de la canción:")
        nombre_cantante = input("Ingrese el nombre del cantante: ")
        grupo = input("Ingrese el nombre del grupo: ")
        cantante = Cantante(nombre_cantante, grupo)
        cancion = Cancion(nombre, duracion, favorita, estrellas, cantante)
        lista.append(cancion)
    return lista

def crearListaNueva():
    nombre = input("Ingrese el nombre de la lista: ")
    creador = input("Ingrese el nombre del creador: ")
    listaCanciones = ListaCanciones(nombre, creador)
    return listaCanciones

def print_error(message):
    print("\n\033[91m\033[1mERROR:\033[0m", message, "\n")

def main():
    print("Bienvenido a la lista de canciones")
    while True:
        print("1. Crear lista con datos de archivo")
        print("2. Crear lista con datos ingresados por el usuario")
        print("3. Ver listas de canciones")
        print("4. Salir")

        opcion = ingresar_entero("Ingrese una opción: ", rango=(1, 4))
        if opcion == 1:
            lista = loadData()
            nombre = input("Ingrese el nombre de la lista: ")
            creador = input("Ingrese el nombre del creador: ")
            listaCanciones = ListaCanciones(nombre, creador)
            listaCanciones.crearLista(lista)
            listadoListas.append(listaCanciones)
            respuesta = input("¿Desea agregar más canciones a la lista? (sí/no): ")
            if respuesta.lower() == "si":
                lista = ingresarCancionesaLista()
                listaCanciones.crearLista(lista)
            else:
                print("No se agregaron canciones extras a la lista.")
        elif opcion == 2:
            listaCanciones = crearListaNueva()
            lista = ingresarCancionesaLista()
            listaCanciones.crearLista(lista)
            listadoListas.append(listaCanciones)

        elif opcion == 3:
            if len(listadoListas) == 0:
                print_error("No hay listas creadas.")
            else:
                for i, lista in enumerate(listadoListas):
                    print(f"{i + 1}. Nombre: {lista.nombre} - Cantidad de canciones: {lista.cantidad} - Duración total: {convertir_minutosfloat(lista.duracion)} - Creador: {lista.creador}")

                seleccion_lista = ingresar_entero("Ingrese el número de la lista a gestionar: ", rango=(1, len(listadoListas)))
                lista = listadoListas[seleccion_lista - 1]

                # Bucle para gestionar el listado de canciones seleccionado
                while True:
                    print("\nGestionando lista de canciones:")
                    print("1. Mostrar lista")
                    print("2. Ordenar lista")
                    print("3. Agregar canciones a la lista")
                    print("4. Volver al menú principal")
                    opcion2 = ingresar_entero("Ingrese una opción: ", rango=(1, 4))

                    if opcion2 == 1:
                        lista.mostrarLista()
                    elif opcion2 == 2:
                        print("Seleccione el atributo por el cual desea ordenar la lista:")
                        print("1. Canción")
                        print("2. Cantante")
                        print("3. Duración")
                        print("4. Estrellas")
                        print("5. Favorita")
                        criterio = ingresar_entero("Ingrese el número correspondiente al atributo: ", rango=(1, 5))
                        atributos = ['nombre', 'cantante.nombre', 'duracion', 'estrellas', 'favorita']
                        lista.ordenarLista(atributos[criterio - 1])
                        lista.mostrarLista()
                    elif opcion2 == 3:
                        nuevas_canciones = ingresarCancionesaLista()
                        lista.crearLista(nuevas_canciones)
                    elif opcion2 == 4:
                        break  # Salir del bucle y volver al menú principal

        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print_error("Opción no válida. Por favor, intente de nuevo.")
main()




