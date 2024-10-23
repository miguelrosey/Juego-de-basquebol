def iniciar_juego():
    while True:
        print("Bienvenid@ al campeonato de baloncesto. ¿Deseas comenzar el juego?")
        print("1. Sí / 2. No")
        inicio = input()

        if inicio == "1":
            print("\nEres el capitán de tu equipo de baloncesto. Es el último cuarto del juego "
                  "y el marcador está empatado. Faltan solo 10 segundos en el reloj.\n")
            print("¿Cuál es tu posición en el equipo?")
            print("1. Base (Controlas el ritmo del juego)")
            print("2. Ala (Eres un tirador habilidoso)")
            print("3. Pívot (Dominas el juego cerca de la canasta)")
            posicion = input()

            if posicion == "1":
                jugar_como_base()
            elif posicion == "2":
                jugar_como_ala()
            elif posicion == "3":
                jugar_como_pivot()

        elif inicio == "2":
            print("Hasta luego.")
            break  # Salir del juego si elige no jugar

def jugar_como_base():
    print("\nEres el base del equipo. Tienes el control del balón y decides cómo jugar el último ataque.")
    print("¿Qué decides hacer?")
    print("1. Jugar rápido y tratar de sorprender al rival")
    print("2. Calmar el ritmo y preparar una jugada organizada")
    decision = input()

    if decision == "1":
        print("\nDecides jugar rápido, pero la defensa te presiona. Debes tomar una decisión inmediata.")
        print("1. Intentar penetrar hacia la canasta")
        print("2. Hacer un tiro de media distancia")
        print("3. Pasar a un compañero en el perímetro")
        accion = input()

        if accion == "1":
            penetrar_canasta()
        elif accion == "2":
            tiro_media_distancia()
        elif accion == "3":
            pasar_perimetro()

    elif decision == "2":
        print("\nOrganizas el ataque y tu equipo se posiciona. Ves a tus compañeros buscando el espacio.")
        print("1. Dar un pase a tu tirador estrella")
        print("2. Buscar una pantalla para liberar tu tiro")
        print("3. Hacer un pick and roll con el pívot")
        jugada = input()

        if jugada == "1":
            pasar_tirador()
        elif jugada == "2":
            buscar_pantalla()
        elif jugada == "3":
            pick_and_roll()

def jugar_como_ala():
    print("\nEres el tirador del equipo, tu entrenador confía en tu capacidad para anotar desde el perímetro.")
    print("¿Qué decides hacer?")
    print("1. Cortar hacia la canasta sin el balón")
    print("2. Moverte hacia el perímetro para recibir el balón y tirar")
    decision = input()

    if decision == "1":
        print("\nCortas hacia la canasta, tu base te ve y te pasa el balón.")
        print("1. Hacer una bandeja")
        print("2. Intentar un tiro acrobático")
        jugada = input()

        if jugada == "1":
            bandeja_exito()
        elif jugada == "2":
            tiro_acrobatico()

    elif decision == "2":
        print("\nTe mueves al perímetro y recibes el balón en la línea de tres puntos.")
        print("1. Tirar rápidamente antes de que la defensa llegue")
        print("2. Amagar el tiro y penetrar hacia la canasta")
        decision_tiro = input()

        if decision_tiro == "1":
            tiro_tres_puntos()
        elif decision_tiro == "2":
            penetrar_y_anotar()

def jugar_como_pivot():
    print("\nEres el pívot del equipo, el ancla en defensa y el poder en la pintura. En esta última jugada, tu equipo necesita de tu presencia física.")
    print("¿Qué decides hacer?")
    print("1. Postearte y pedir el balón cerca de la canasta")
    print("2. Bloquear para liberar a tus compañeros")
    decision = input()

    if decision == "1":
        print("\nTe postean bajo el aro, recibes el balón.")
        print("1. Hacer un gancho")
        print("2. Girar rápidamente y hacer una bandeja")
        decision_poste = input()

        if decision_poste == "1":
            gancho()
        elif decision_poste == "2":
            giro_bandeja()

    elif decision == "2":
        print("\nBloqueas a un defensor y liberas a tu compañero tirador.")
        print("1. Continuar hacia la canasta para un pase rápido")
        print("2. Quedarte en la pintura para un rebote")
        decision_bloqueo = input()

        if decision_bloqueo == "1":
            pase_rapido()
        elif decision_bloqueo == "2":
            pelear_rebote()

# Funciones finales y desenlaces del juego
def tiro_tres_puntos():
    print("\nLanzas el tiro de tres puntos justo antes de que suene el silbato. ¡Encesta! "
          "Tu equipo gana dramáticamente con un tiro en el último segundo.\n"
          "-Final 1: ¡Victoria épica con un tiro de tres puntos!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def tiro_media_distancia():
    print("\nTe detienes y lanzas desde media distancia. El balón golpea el aro, da vueltas... ¡y entra! "
          "Tu equipo celebra la victoria.\n"
          "-Final 2: ¡Victoria con tiro de media distancia!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def penetrar_canasta():
    print("\nPenetras hacia la canasta, pero la defensa te bloquea. Pierdes el balón y el partido se va a tiempo extra.\n"
          "-Final 3: Perdiste la oportunidad, el rival gana en tiempo extra-\n"
          "Gracias por jugar.")
    preguntar_volver()

def pasar_perimetro():
    print("\nPasas el balón a un compañero en el perímetro, pero falla el tiro en el último segundo.\n"
          "-Final 4: El rival gana en tiempo extra-\n"
          "Gracias por jugar.")
    preguntar_volver()

def bandeja_exito():
    print("\nHaces una bandeja limpia y el balón entra justo antes del final del juego. "
          "Tu equipo celebra la victoria.\n"
          "-Final 5: ¡Victoria con una bandeja en el último segundo!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def tiro_acrobatico():
    print("\nIntentas un tiro acrobático, pero el balón no entra. La defensa recupera el balón y el tiempo se acaba.\n"
          "-Final 6: Derrota en el último segundo-\n"
          "Gracias por jugar.")
    preguntar_volver()

def penetrar_y_anotar():
    print("\nAmagas el tiro, penetras hacia la canasta y anotas un tiro decisivo justo antes de que suene el final.\n"
          "-Final 7: ¡Victoria con una penetración valiente!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def gancho():
    print("\nHaces un gancho perfecto, el balón entra limpiamente y tu equipo gana.\n"
          "-Final 8: ¡Victoria con un gancho en el último segundo!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def giro_bandeja():
    print("\nGiras rápidamente y haces una bandeja, pero el balón se sale del aro en el último momento. "
          "Tu equipo pierde la oportunidad.\n"
          "-Final 9: Derrota por un giro fallido-\n"
          "Gracias por jugar.")
    preguntar_volver()

def pase_rapido():
    print("\nRecibes el pase rápido y haces una volcada espectacular para ganar el juego.\n"
          "-Final 10: ¡Victoria con volcada decisiva!-\n"
          "Gracias por jugar.")
    preguntar_volver()

def pelear_rebote():
    print("\nTe quedas bajo la canasta, peleas el rebote y logras anotar antes de que el tiempo se acabe.\n"
          "-Final 11: ¡Victoria tras pelear el rebote!-\n"
          "Gracias por jugar.")
    preguntar_volver()

# Función para reiniciar o salir del juego
def preguntar_volver():
    while True:
        print("¿Quieres volver a jugar?")
        print("1. Sí / 2. No")
        volver = input()
        if volver == "1":
            iniciar_juego()
        elif volver == "2":
            print("Hasta luego.")
            break

# Iniciamos el juego
iniciar_juego()
