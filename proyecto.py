import random
class Ejercicio:
    def __init__(self):
        self.resultados = []

    def generar_ejercicio(diccionario, num_palabras):
        with open(diccionario,'r') as file:
            palabras = file.read().split()

        texto_random = ' '.join(random.choices(palabras, k=num_palabras))
        return texto_random
    def pulsacion(self):
        pass
    def resultado(self):
        pass
#Historial de usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_ejercicios = []
        self.estadisticas = {}

    def guardar_resultado(self):
        pass
    def procesar_resultado(self):
        pass
    def configurar_usuario(self):
        pass

#Interfaz
class Interfaz:
    def __init__(self):
        pass
    def menu_principal(self):
        pass
    def menu_configuracion(self):
        pass