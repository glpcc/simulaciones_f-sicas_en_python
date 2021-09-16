import random
from numpy.lib.function_base import select
import pygame
import numpy as np 
import random
import math

class Ball():
    def __init__(self,radious,initial_vel,initial_pos):
        self.radious = radious
        self.velocity = initial_vel
        self.position = initial_pos
        self.color = [random.randint(0,255) for i in range(3)]
    def update(self):
        self.position += self.velocity

    def draw(self,canvas):
        pygame.draw.circle(canvas,self.color,self.position,self.radious)
    
    def test_collisions_with_other_balls(self,balls):
        for ball in balls:
            if np.linalg.norm([ball[0]-self.position[0],ball[1]-self.position[1]]) <= self.radious:
                self.elastic_collision(ball)



    def test_borders(self,borders):
        # borders would come in format in side a np array like [[first_point],[border_vector]]
        for border in borders:
            border_length = np.linalg.norm(border[1])
            if self.distance_to_border(border) <= self.radious:
                if np.linalg.norm([border[0][0]-self.position[0],border[0][1]-self.position[1]])-self.radious <= border_length and np.linalg.norm([(border[0][0]+border[1][0])-self.position[0],(border[0][1]+border[1][1])-self.position[1]])-self.radious <= border_length:
                    border_perp = np.array([border[1][1],-border[1][0]])
                    self.velocity -= 2*((np.dot(border_perp,self.velocity)/border_length**(2))*border_perp)
                    
    def elastic_collision(self,ball):
        self.velocity,ball.velocity = ball.velocity,self.velocity

    def distance_to_border(self,border):
        border_point2x = border[0][0] + border[1][0]
        border_point2y = border[0][1] + border[1][1]
        
        # use the formula of the distance from a line to a point
        distance = abs((border_point2y-border[0][0])*(border[0][1]-self.position[1])-(border[0][0]-self.position[0])*(border_point2y-border[0][1]))/np.linalg.norm([border_point2x-border[0][0],border_point2y-border[0][1]])
        return distance


        

