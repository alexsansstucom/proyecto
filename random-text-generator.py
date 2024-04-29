import random

def generar_texto_random(diccionario, num_palabras):
    with open(diccionario, 'r') as file:
        palabras = file.read().split()

    texto_random = ' '.join(random.choices(palabras, k=num_palabras))
    return texto_random
    cghvh
diccionario = 'diccionario.txt'
num_palabras = 100

texto_random = generar_texto_random(diccionario, num_palabras)
print(texto_random)
