# Importación de las bibliotecas necesarias
import pygame as pygame
from pygame.math import Vector2 as V2
from random import randint as rnd

try:
    # Definición de la función para generar la posición aleatoria de la comida y inicialización de Pygame
    food, _ = lambda: V2(rnd(0,14), rnd(0,14)), pygame.init()

    # Creación de la ventana del juego y definición de la tecla especial
    DISP, KEY = pygame.display.set_mode((600,600)), 1073741903

    # Inicialización de variables importantes para el juego
    pcs, fd, dr = [V2(7,7)], food(), V2(-1,0)

    # Diccionario para mapear teclas a vectores de dirección
    drs = {0: V2(1,0), 1: V2(-1,0), 2: V2(0,1), 3: V2(0,-1)}

    # Bucle principal del juego
    while pcs.count(pcs[0]) == 1:
        # Limpieza de la pantalla con un color negro
        DISP.fill('black')

        # Manejo de eventos de Pygame
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if e.type == pygame.KEYDOWN:
                dr = drs.get(e.key - KEY, dr)

        # Si la cabeza de la serpiente alcanza la comida, se genera una nueva posición aleatoria para la comida y se incrementa la longitud de la serpiente
        if pcs[0] == fd:
            fd, pcs = food(), pcs + [pcs[0]]

        # Dibujo de las partes del cuerpo de la serpiente y la comida
        for pc in pcs:
            pygame.draw.rect(DISP, 'green', (*40*pc, 40, 40))
        pygame.draw.rect(DISP, 'red', (*40*fd, 40, 40))

        # Actualización de la posición de la serpiente
        pcs.insert(0, pcs[0] + dr)
        pcs.pop(-1)

        # Ajuste de las coordenadas de la cabeza de la serpiente para que permanezca dentro de los límites del juego
        pcs[0].x, pcs[0].y = pcs[0].x % 15, pcs[0].y % 15

        # Actualización de la pantalla del juego
        pygame.display.update()

        # Espera breve antes de la siguiente iteración del bucle
        pygame.time.wait(100)

except pygame.error as err:
    # Manejo de errores específicos de Pygame
    print("Error de Pygame:", err)
except Exception as ex:
    # Manejo de otros errores inesperados
    print("Error inesperado:", ex)