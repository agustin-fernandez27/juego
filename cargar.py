import json
import csv
from random import shuffle

"""primero se importa el CSV y se cargan los datos
    """
# Carga Partidas (csv)

def cargar_partidas():
    partidas = []
    try:
        with open("partidas.csv", "r",encoding= "UTF-8") as f:
            lector = list(csv.reader(f))
            i = 1  
            while i < len(lector):
                fila = lector[i]

                nivel = int(fila[0])
                partida = int(fila[1])
                letras = fila[2]
                palabras_crudas = fila[3].split(";")

                palabras = []
                j = 0
                while j < len(palabras_crudas):
                    palabras.append(palabras_crudas[j])
                    j += 1

                partidas.append({
                    "nivel": nivel,
                    "partida": partida,
                    "letras": letras,
                    "palabras": palabras
                })

                i += 1
    except:
        print("Error cargando partidas.csv")

    shuffle(partidas)
    return partidas
    
""" se abre el JSON, verifica si hay usuarios y si no hay los crea
    """
# Guardado Usuarios JSON

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except:
        return []

def guardar_usuarios(usuarios):
    texto = json.dumps(usuarios)
    with open("usuarios.json", "w") as f:
        f.write(texto)
