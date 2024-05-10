
class Pulsacion:
    def __init__(self):
        self.resultados = []
        self.ejercicio_terminado = False
        self.teclas_correctas = ["a", "s", "d", "f", "j", "k", "l", ";"]
        self.ultimo_timestamp = None

    def comparar_pulsacion(self, tecla_usuario):
        if self.ejercicio_terminado:
            return 0  # Ejercicio ya terminado

        timestamp = time.time()
        tecla_correcta = self.teclas_correctas[len(self.resultados) % len(self.teclas_correctas)]
        correcto = tecla_usuario == tecla_correcta

        registro = {
            "timestamp": timestamp,
            "tecla_correcta": tecla_correcta,
            "tecla_usuario": tecla_usuario,
            "correcto": correcto
        }

        self.resultados.append(registro)
        self.ultimo_timestamp = timestamp

        if correcto:
            return 1  # Pulsación correcta
        else:
            return -1  # Pulsación incorrecta

    def terminar_ejercicio(self):
        self.ejercicio_terminado = True
for pulsacion in pulsaciones_usuario:
    resultado = tutor.comparar_pulsacion(pulsacion)
    print("Resultado:", resultado)
