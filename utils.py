
import re
# Convierte el tiempo float en minutos a mm:ss
def convertir_minutosfloat(duracion):
    minutos = int(duracion)
    segundos = round((duracion - minutos) * 60)
    return f"{minutos}:{segundos:02d}"


def minutosToFloat(duracion):
    duracion = duracion.replace(" ","")
    if not re.match(r"^\d+(:\d{1,2})?$", duracion):
        raise ValueError("El formato de duración no es válido.")

    # Separamos minutos y segundos si están disponibles
    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1]) if len(partes) == 2 else 0

    # Validamos que los segundos no sean mayores a 59 y que los minutos y segundos no sean negativos
    if segundos > 59 or minutos < 0 or segundos < 0:
        raise ValueError("Los valores de minutos o segundos no son válidos.")

    return minutos + segundos / 60

def print_error(message):
    print("\n\033[91m\033[1mERROR:\033[0m", message, "\n")