import random

def generar_texto_random(diccionario, num_palabras):
    with open(diccionario, 'r') as file:
        palabras = file.read().split()

    texto_random = ' '.join(random.choices(palabras, k=num_palabras))
    return texto_random
    input()
texto_random = generar_texto_random(diccionario, num_palabras)
print(texto_random)
