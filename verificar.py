from juego import *
from cargar import *
from random import *

def mezclar_letras(letras):
    lista = []
    i = 0
    while i < len(letras):
        lista.append(letras[i])
        i += 1
    shuffle(lista)
    return "".join(lista)

def es_palabra_valida(palabra, lista):
    i = 0
    while i < len(lista):
        if palabra == lista[i]:
            return True
        i += 1
    return False
