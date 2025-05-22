import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

ejectutar = True
while ejectutar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejectutar = False