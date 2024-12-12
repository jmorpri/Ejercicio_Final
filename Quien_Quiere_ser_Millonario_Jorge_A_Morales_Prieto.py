import request
import random

def obten_preguntas():
    url = "https://opentdb.com/api.php?amount=15&category=15&difficulty=easy&type=multiple"
    respuesta = request.get(url)
    datos = respuesta.json()
    return datos["results"]

def mostrar_pregunta(pregunta, numero):
    print(f"\nPregunta {numero}: {pregunta["question"]}")
    opciones = pregunta["incorrect_answer"] + [pregunta["corret_answer"]]
    random.shuffle(opciones)
    for i, opciones in enumerate(opciones, 1):
        print(f"{i}. {opciones}")
    return opciones

def iniciar_juego():
    nombre = input("Bienvenido a ¿Quién quiere ser millonario Cual es tu Nombre:")

    preguntas = obten_preguntas()
    puntos = 0
    comodin_usado = False

    for i, pregunta in enumerate(pregunta, 1):
        print(f"\nPuntos actuales: {puntos}")
        decision = input("¿Desea continuar o plantarte? c/p: ").lower()
        if decision == "p":
            print(f"Te has plantado con {puntos} puntos. ¡Gracias por Jugar!")
            return
        if not comodin_usado:
            usar_comodin == input("¿Deseas usar tu comodín para saltar esta pregunta? (s/n): ").lower()
            if usar_comodin == "s":
                comodin_usado = True
                print("Comodín usado. Saltar pregunta ...")

        opciones = mostrar_pregunta(pregunta, i)
        respuesta_usuario = input("Elige tu respuesta (1-4):")

        try:
            indice_repuesta = int(respuesta_usuario) - 1
            if opciones[indice_repuesta] == pregunta["correct_answer"]:
                print("¡Correcto! Sumaste un punto.")
                puntos += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta["correct_answer"]}")
                print("Has perdido a casa. Tu puntuacion final es 0.")
                return
        except (ValueError, IndexError):
            print("Opción inválida. Por favor, selecciona un número entre 1 y 4.")

    print(f"\n¡Felicidades, {nombre}! Ganaste, Tu puntuación Final es: {puntos}")


if  __name__ == "__main__":
    iniciar_juego()