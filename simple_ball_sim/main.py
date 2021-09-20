import pygame
from pygame.locals import *
import random
import numpy as np
from ball import Ball


def test_of_solid_body(test_balls,velocity):
    for ball in test_balls:
        ball.velocity = velocity

def draw_borders(canvas,borders):
    for i in borders:
        pygame.draw.line(canvas,(255,255,255),(i[0][0],i[0][1]),(i[0][0]+i[1][0],i[0][1]+i[1][1]))

window_height = 800
window_width = 1000
canvas = pygame.display.set_mode((window_width,window_height))
pygame.init()
runnig = True

walls = np.array([
    [[0,0],[window_width,0]],
    [[window_width,0],[0,window_height]],
    [[window_width,window_height],[-window_width,0]],
    [[0,window_height],[0,-window_height]],
    [[600,800],[200,-100]]
    
    ])
test_balls = [Ball(20,np.array([0.1,0.1]),np.array([float((50*(i%5)) +100),float((50*(i//5)) + 100)]))for i in range(20)]
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    canvas.fill((0,0,0))
    for i in range(len(test_balls)):
        if test_balls[i].test_borders(walls):
            test_of_solid_body(test_balls,test_balls[i].velocity)
        test_balls[i].test_collisions_with_other_balls(test_balls[i+1:])
        test_balls[i].update()
        test_balls[i].draw(canvas)

    draw_borders(canvas,walls)
    pygame.display.flip()



pygame.quit()