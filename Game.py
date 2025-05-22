import pygame

# Inicializador
pygame.init()

# Crear la ventana
pantalla = pygame.display.set_mode((800, 600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Jugador

img_jugador = pygame.image.load("nave.png")
jugador_x = 330
jugador_y = 450
jugador_x_cambio = 0
jugador_y_cambio = 0

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Bucle principal
ejecutar = True
while ejecutar:

    # RGB
    pantalla.fill((205, 144, 228))


    # Eventos
    for event in pygame.event.get():

        # Cerrar
        if event.type == pygame.QUIT:
            ejecutar = False

        # Presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio -= .25
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio += .25

        # Soltar teclas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0



    # Movimiento del jugador
    jugador_x += jugador_x_cambio

    # Bordes
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 640:
        jugador_x = 640

    jugador(jugador_x, jugador_y)


    # Actualizar la pantalla
    pygame.display.update()
