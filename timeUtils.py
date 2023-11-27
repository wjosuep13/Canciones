    # Convierte el tiempo float en minutos a mm:ss
def convertir_minutosfloat(duracion):
    minutos = int(duracion)
    segundos = round((duracion - minutos) * 60)
    return f"{minutos}:{segundos:02d}"