import random
import pygame
import numpy as np 
import random
import math

class ball():
    def __init__(self,radious,initial_vel,initial_pos):
        self.radious = radious
        self.velocity = initial_vel
        self.position = initial_pos
        self.color = [random.randint(0,255) for i in range(3)]
    def update(self):
        self.position += self.velocity

    def draw(self,canvas):
        pygame.draw.rect(canvas,self.color,self.position,self.radious)
    
    def test_collisions_with_other_balls(self,balls):
        for ball in balls:
            if (math.sqrt((self.position[0]-ball.position[0])**(2)+(self.position[1]-ball.position[1])) <= self.radious):
                self.elastic_collision(ball)
    def test_borders(self,borders):
        for border in borders:
            border_length = np.linalg.norm(border)
            self.velocity += 2*()
    def elastic_collision(self,ball):
        self.velocity,ball.velocity = ball.velocity,self.velocity



        

