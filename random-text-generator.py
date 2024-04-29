import random

def generar_text_random(diccionario, num_palabras):
    with open(diccionario, 'r') as file:
        palabras = file.read().split()

    texto_random = ' '.join(random.choices(palabras, k=num_palabras))
    return texto_random