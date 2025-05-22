import pygame
import random

# Inicializador
pygame.init()

# Crear la ventana
pantalla = pygame.display.set_mode((800, 600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Jugador

img_jugador = pygame.image.load("nave.png")
jugador_x = 400
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0

# Enemigo

img_enemigo = pygame.image.load("ovni.png")
enemigo_x = random.randint(0, 758)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 30

# Funcion para dibujar el jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion para dibujar el enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Bucle principal
ejecutar = True
while ejecutar:

    # Imagen
    pantalla.blit(fondo, (0, 0))


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

    # Borde Jugador
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 758:
        jugador_x = 758

        # Movimiento del enemigo
    enemigo_x += enemigo_x_cambio

    # Borde Enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 758:
        enemigo_x_cambio = -0.1
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)


    # Actualizar la pantalla
    pygame.display.update()
