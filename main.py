import pygame
from pygame.locals import *
import math
import numpy as np
from ball import Ball


window_height = 800
window_width = 1000
canvas = pygame.display.set_mode((window_width,window_height))
pygame.init()
runnig = True

walls = np.array([[[0,0],[window_width,0]],[[window_width,0],[0,window_height]],[[window_width,window_height],[-window_width,0]],[[0,window_height],[0,-window_height]]])
test_ball = Ball(20,np.array([0.1,-1.]),np.array([200.,200.]))
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    canvas.fill((0,0,0))
    test_ball.test_borders(walls)
    test_ball.update()
    test_ball.draw(canvas)
    pygame.display.flip()

pygame.quit()