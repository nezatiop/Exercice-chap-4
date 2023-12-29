import pygame
import sys
import math
"""
#Exercice 4.6.1
pygame.init()

noir = (255,255,255)
blanc = (0,0,0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((2000, 1000))
pygame.display.set_caption("Polygone Régulier")


def dessin_polygone(surface, cote):
    centre = (1000,500)
    rayon = 300
    points = []
    for i in range(cote):
        angle = i * (2 * math.pi) / cote
        x = int(centre[0] + rayon * math.cos(angle))
        y = int(centre[1] + rayon * math.sin(angle))
        points.append((x,y))

    for i in range(cote):
        pygame.draw.line(surface, noir, points[i], points[(i+1)%cote])

cote = int(input())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    clock.tick(60)

    screen.fill(blanc)
    dessin_polygone(screen,cote)    

    pygame.display.flip()

    if event.key == pygame.K_ESCAPE:
        event.type == pygame.QUIT
"""
