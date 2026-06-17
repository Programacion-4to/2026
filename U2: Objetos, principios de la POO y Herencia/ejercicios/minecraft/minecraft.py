# Mini Minecraft 2D
# Leé el enunciado en enunciado.md
# El diseño (constantes, colores y ventana) ya está armado.
# Ustedes deben implementar TODAS las clases y la lógica.

import pygame

# --- Diseño ---
TAM = 32
COLS = 25
FILAS = 18
ANCHO = COLS * TAM
ALTO = FILAS * TAM + 70
FPS = 60

# Colores de los bloques
COLOR_TIERRA = (134, 96, 67)
COLOR_PIEDRA = (130, 130, 130)
COLOR_MADERA = (181, 101, 29)

# Colores generales
COLOR_CIELO = (110, 180, 230)
COLOR_BORDE_BLOQUE = (30, 30, 30)
COLOR_HUD = (40, 40, 40)
COLOR_TEXTO = (255, 255, 255)
COLOR_SELECCION = (255, 255, 0)

# Personaje
COLOR_CUERPO = (60, 90, 160)
COLOR_PIEL = (240, 200, 160)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mini Minecraft 2D")
    reloj = pygame.time.Clock()

    # TODO: instanciar acá los objetos del juego (mundo, jugador, etc.)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            # TODO: manejar el resto de los eventos (teclas, mouse, etc.)

        # TODO: actualizar y dibujar el estado del juego

        pantalla.fill(COLOR_CIELO)
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
