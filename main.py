from Cantante import Cantante
from Cancion import Cancion
from ListaCanciones import ListaCanciones
import csv

def preloadData():
    # se lee el archivo canciones.csv con la data omitiendo el encabezado
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  #omite el encabezado
        for row in csv_reader:
            print(row)

def main():

    print("Bienvenido a la lista de canciones")
    print("1. Crear nueva lista de canciones")
    print("2. Cargar datos del archivo")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))

    while opcion != 3:
        if opcion == 1:
            print("Ingrese los datos de la lista de canciones")
            nombre = input("Ingrese el nombre de la lista: ")
            creador = input("Ingrese el nombre del creador: ")
            #preguntar cuantas canciones quiere crear
            cantidad = int(input("Ingrese la cantidad de canciones a crear: "))
            lista = []
            for i in range(cantidad):
                print("Ingrese los datos de la cancion")
                nombre = input("Ingrese el nombre de la cancion: ")
                duracion = int(input("Ingrese la duracion de la cancion: "))
                favorita = input("Ingrese si la cancion es favorita: ")
                estrellas = int(input("Ingrese la cantidad de estrellas: "))
                print("Ingrese los datos del cantante de la cancion")
                nombre = input("Ingrese el nombre del cantante: ")
                grupo = input("Ingrese el nombre del grupo: ")
                cantante = Cantante(nombre, grupo)
                cancion = Cancion(nombre, duracion, favorita, estrellas, cantante)
                lista.append(cancion)
            ListaCanciones.crearLista(cancion)
            print("1. Crear lista de canciones")
            print("2. Salir")
            opcion = int(input("Ingrese una opcion: "))
        elif opcion == 2:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")
            print("1. Crear lista de canciones")
            print("2. Salir")
            opcion = int(input("Ingrese una opcion: "))

