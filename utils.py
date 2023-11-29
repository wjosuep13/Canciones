
import re
# Convierte el tiempo float en minutos a mm:ss
def convertir_minutosfloat(duracion):
    minutos = int(duracion)
    segundos = round((duracion - minutos) * 60)
    return f"{minutos}:{segundos:02d}"


def minutosToFloat(duracion):
    duracion = duracion.replace(" ", "")

    # Acepta formatos mm:ss y mm
    if not re.match(r"^\d{1,2}(:\d{1,2})?$", duracion):
        print_error("El formato de duración no es válido. Debe ser mm:ss o mm.")
        return 0.0

    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1]) if len(partes) == 2 else 0

    # Valida los minutos y segundos
    if segundos > 59 or minutos < 0 or segundos < 0:
        print_error("El formato de duración no es válido. Debe ser mm:ss o mm.")
        return 0.0

    return minutos + segundos / 60.0

def print_error(message):
    print("\n\033[91m\033[1mERROR:\033[0m", message, "\n")