import pygame
from pygame.locals import *
import math

canvas = pygame.display.set_mode((1000,1000))
pygame.init()
runnig = True




while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    
    canvas.fill((0,0,0))
            

    pygame.display.flip()

pygame.quit()