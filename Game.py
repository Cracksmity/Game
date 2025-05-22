import pygame

# Inicializador
pygame.init()

# Crear la ventana
pantalla = pygame.display.set_mode((800, 600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Bucle principal
ejectutar = True
while ejectutar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejectutar = False

    pantalla.fill((205, 144, 228))
    pygame.display.update()
