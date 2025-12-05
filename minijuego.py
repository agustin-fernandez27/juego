import random

def crear_matriz(v) -> list:
    filas = 5
    columnas = 5
    matriz = []
    for i in range(filas):
        fila = [v] * columnas
        matriz.append(fila)
    fila_random = random.randint(0, filas-1)
    columna_random = random.randint(0, columnas-1)
    matriz[fila_random][columna_random]= "🎁"

    return matriz, fila_random, columna_random, filas, columnas

def ingresar():
    while True:  
        ingreso_fila = int(input("Ingrese una posición entre 0 y 4 (fila): "))
        ingreso_columna = int(input("Ingrese una posición entre 0 y 4 (columna): "))

        if 0 <= ingreso_fila <= 4 and 0 <= ingreso_columna <= 4:
            return ingreso_fila, ingreso_columna  
        else:
            print("Ingrese un número entre 0 y 4.")

def burbujear(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
  #---------modulo_base-----------------------------------------------------------
  def manipular_fila(matriz, ingreso_fila, columnas):
    for j in range(columnas):
        if matriz[ingreso_fila][j] == "🎁":
            return True
    return False

def manipular_columna(matriz, ingreso_columna, filas):
    for i in range(filas):
        if matriz[i][ingreso_columna] == "🎁":
            return True
    return False

def manipular_principal(matriz, filas):
    for i in range(filas):
        if matriz[i][i] == "🎁":
            return True
    return False

def manipular_secundaria(matriz, filas, columnas):
    for i in range(filas):
        if matriz[i][columnas - 1 - i] == "🎁":
            return True
    return False

def ubicar(matriz, ingreso_fila, ingreso_columna, filas, columnas):

    if manipular_fila(matriz, ingreso_fila, columnas):
        print("La recompensa está en tu fila")

    if manipular_columna(matriz, ingreso_columna, filas):
        print("La recompensa está en tu columna")

    if manipular_principal(matriz, filas) and ingreso_fila == ingreso_columna:
        print("La recompensa está en tu diagonal principal")

    if manipular_secundaria(matriz, filas, columnas) and ingreso_fila + ingreso_columna == columnas - 1:
        print("La recompensa está en tu diagonal secundaria")

    return
  #----------modulo_manipular-------------------------------------------------------------
  from manipulacion import *
from base import *

def jugar(matriz,fila_random,columna_random,intentos,filas,columnas,ingresos):
    if intentos == 0:
        print("Intentos agotados")
        return False
    
    ingreso_fila, ingreso_columna = ingresar()
    ingresos = ingresos + [(ingreso_fila, ingreso_columna)]

    burbujear(ingresos)

    if ingreso_fila == fila_random and ingreso_columna == columna_random:
        print("¡Recompensa encontrada!")
        return True

    print(f"No se encontró la recompensa \n -Ingresos usados: {ingresos}-")
    ubicar(matriz, ingreso_fila, ingreso_columna, filas, columnas)

    return jugar(
        matriz,
        fila_random,
        columna_random,
        intentos - 1,
        filas,
        columnas,
        ingresos
    )

matriz, fila_random, columna_random, filas, columnas = crear_matriz("❌")
ingresos = []
jugar(matriz, fila_random, columna_random, intentos=3, filas=filas, columnas=columnas, ingresos=ingresos,)
for fila in matriz:
    print(fila)
