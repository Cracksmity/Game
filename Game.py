import pygame
import random
import math

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

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 6

for i in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("ovni.png"))
    enemigo_x.append(random.randint(0, 758))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(30)

# Municion
img_municion = pygame.image.load("bala.png")
bala_x = 0
bala_y = 536
bala_x_cambio = 0
bala_y_cambio = .2
bala_visible = False

# Puntaje
puntaje_jugador = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# Funcion para dibujar el jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion para dibujar el enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion para disparar la municion
def disparar_municion(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_municion, (x, y))

# Funcion Colisiones
def colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    if distancia < 20:
        return True
    else:
        return False


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
    for i in range(cantidad_enemigos):
        enemigo_x[i] += enemigo_x_cambio[i]

    # Borde Enemigo
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.1
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 758:
            enemigo_x_cambio[i] = -0.1
            enemigo_y[i] += enemigo_y_cambio[i]

        # Colision
        colision = colisiones(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if colision:
            bala_y = jugador_y
            bala_visible = False
            puntaje_jugador += 1
            enemigo_x[i] = random.randint(0, 758)
            enemigo_y[i] = random.randint(50, 200)

        enemigo(enemigo_x[i], enemigo_y[i], i)

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


    # Actualizar la pantalla
    pygame.display.update()