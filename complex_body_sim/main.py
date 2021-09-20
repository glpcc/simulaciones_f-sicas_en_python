from body import body
import numpy as np
import pygame



def generate_square(up_corner,width,height):
    points = np.array([[up_corner[0],up_corner[1]],[up_corner[0]+width,up_corner[1]],[up_corner[0]+ width,up_corner[1] + height],[up_corner[0],up_corner[1]+height]])
    return points

square_points = generate_square([200,200],600,50)
square = body(square_points,1)

obstacles = np.array([
    [[400.,300.],[400.,800.]]
    
])


window_height = 800
window_width = 1000
canvas = pygame.display.set_mode((window_width,window_height))
pygame.init()
runnig = True


while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    canvas.fill((0,0,0))

    for obstacle in obstacles:
        pygame.draw.lines(canvas,(255,255,255),True,obstacle)

    square.update_grav()
    #square.sim_collisions(obstacles)
    square.update()
    square.draw(canvas)

    pygame.display.flip()



pygame.quit()