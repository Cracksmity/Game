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

# Municion
img_municion = pygame.image.load("bala.png")
bala_x = 0
bala_y = 536
bala_x_cambio = 0
bala_y_cambio = .2
bala_visible = False

# Funcion para dibujar el jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion para dibujar el enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Funcion para disparar la municion
def disparar_municion(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_municion, (x, y))

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
            if event.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x + (img_jugador.get_width() // 2) - (
                                img_municion.get_width() // 2)  # Centra la bala horizontalmente
                    bala_y = jugador_y  # La bala aparecerá desde la nave
                    bala_visible = True

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

    # Movimiento de la municion
    if bala_visible:
        bala_y -= bala_y_cambio
        if bala_y <= 0:  # Si la bala llega al tope de la pantalla
            bala_visible = False  # La bala deja de ser visible
            bala_y = jugador_y  # Reset de la posición Y de la bala
            bala_x = jugador_x  # Reset de la posición X de la bala
        else:
            disparar_municion(bala_x, bala_y)

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)


    # Actualizar la pantalla
    pygame.display.update()