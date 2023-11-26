from Cantante import Cantante
from Cancion import Cancion
from ListaCanciones import ListaCanciones
import csv
lista_ListaCanciones = []
def loadData():
    lista=[]
    filename = 'canciones.csv'
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_dict_reader = csv.DictReader(file)
        # Itera sobre todas las filas del archivo
        for row in csv_dict_reader:
            # Accede a cada valor por el nombre de la columna
            cancion = row['Cancion']
            cantante = row['Cantante']
            album = row['Album']
            duracion = row['Duracion']
            estrellas = row['Estrellas']
            grupo = row['Grupo']
            favorita = row['Favorita']  
            cantante = Cantante(cantante, grupo)
            cancion = Cancion(cancion, duracion, favorita, estrellas, cantante)
            lista.append(cancion)
    
    
        

def crearlistanueva():
    print("Ingrese los datos de la lista de canciones")
    #preguntar cuantas canciones quiere crear
    cantidad = int(input("Ingrese la cantidad de canciones a agregar: "))
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
    listaCanciones = ListaCanciones(nombre, creador)
    listaCanciones.crearLista(cancion)
    return listaCanciones

def agregarCanciones(listaCanciones, lista):
    listaCanciones.crearLista(lista)
    return listaCanciones

def main():

    print("Bienvenido a la lista de canciones")
    print("1. Crear lista con datos de archivo")
    print("2. Crear lista con datos ingresados por el usuario")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))

    while opcion != 3:
        if opcion == 1:
            #preguntar si desea agregar canciones a la lista
            print("1. Agregar canciones a la lista")
            print("2. No agregar canciones a la lista")
            opcion2 = int(input("Ingrese una opcion: "))
            if(opcion2 == 1):
                listaCanciones = loadData()
                cantidad = int(input("Ingrese la cantidad de canciones a agregar: "))
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

                nombre = input("Ingrese el nombre de la lista: ")
                creador = input("Ingrese el nombre del creador: ")
                listaCanciones = ListaCanciones(nombre, creador)
                listaCanciones.crearLista(cancion)
                return listaCanciones

            
            lista_ListaCanciones.append(listaCanciones)
            opcion = int(input("Ingrese una opcion: "))
        elif opcion == 2:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")
            print("1. Crear lista de canciones")
            print("2. Salir")
            opcion = int(input("Ingrese una opcion: "))

