from datos import *
from random import *
from cargar import *
from verificar import *
import csv
import json

def jugar_partida(partida):
    letras = partida["letras"]
    palabras_validas = partida["palabras"]
    usadas = []
    puntaje = 0
    errores = 0
    terminado = False

    while not terminado:
        print("\nLetras:", letras)
        print("Opciones: Shuffle | Clear | Submit ")
        entrada = input("Ingrese una palabra: ")
        if es_palabra_valida(entrada, palabras_validas):
            puntos = len(entrada)
            puntaje += puntos
            usadas.append(entrada)
            print("Correcto! +", puntos)
            if len(usadas) == len(palabras_validas):
                print("Partida completa!")
                terminado = True
        else:
            print("Incorrecto")
            errores += 1

    return puntaje, errores

def jugar():
    usuarios = cargar_usuarios()

    nombre = input("Usuario: ")
    clave = input("Contraseña: ")

    usuario = None
    i = 0
    while i < len(usuarios):
        if usuarios[i]["usuario"] == nombre and usuarios[i]["password"] == clave:
            usuario = usuarios[i]
            break
        i += 1

    if usuario is None:
        usuario = {"usuario": nombre, "password": clave, "puntaje": 0, "errores": 0}
        usuarios.append(usuario)

    partidas = cargar_partidas()

    nivel = 1
    puntaje_total = 0
    errores_total = 0

    while nivel <= 5:
        print("\n=== NIVEL", nivel, "===")

        nivel_partidas = []
        i = 0
        while i < len(partidas):
            if partidas[i]["nivel"] == nivel:
                nivel_partidas.append(partidas[i])
            i += 1

        j = 0
        puntaje_nivel = 0
        errores_nivel = 0

        while j < len(nivel_partidas):
            p, e = jugar_partida(nivel_partidas[j])
            puntaje_nivel += p
            errores_nivel += e
            j += 1

        puntaje_total += puntaje_nivel
        errores_total += errores_nivel

        print("\nResumen Nivel", nivel)
        print("Puntaje:", puntaje_nivel)
        print("Errores:", errores_nivel)
        print("Tiempo restante: N/A")

        nivel += 1

    usuario["puntaje"] += puntaje_total
    usuario["errores"] += errores_total

    guardar_usuarios(usuarios)

    print("\nJuego completo!")
    print("Puntaje total:", puntaje_total)
    print("Errores totales:", errores_total)

jugar()
