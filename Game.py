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

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Bucle principal
ejecutar = True
while ejecutar:

    # RGB
    pantalla.fill((205, 144, 228))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False


    jugador(jugador_x, jugador_y)

    pygame.display.update()
