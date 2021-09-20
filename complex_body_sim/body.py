import pygame
import numpy as np
import math
class body():
    def __init__(self,points,point_mass):
        self.points = points
        self.point_mass = point_mass
        self.points_velocity = [[0,0] for i in range(len(points))]


    def update(self):
        for i in range(len(self.points)):
            self.points[i] += self.points_velocity[i]

    def update_grav(self):
        for i in self.points_velocity:
            i += [0,9.8/100]

    def sim_collisions(self,obstacles):
        for obstacle in obstacles:
            for obstacle_point in obstacle:
                for i in range(len(self.points)):
                    if self.check_collisions(np.array([self.points[i],self.points[(i+1)%len(self.points)]]),obstacle_point) <= 0:
                        self.collisions_physics(obstacle_point)


    def collisions_physics(self,collision_point):
        body_torque = 0
        for point in self.points:
            point_force = 9.8*self.point_mass
            angle = (math.pi/2) - math.atan((point[1]-collision_point[1])/(point[0]-collision_point[0]))
            body_torque += self.distance_between_points(collision_point,point)*point_force*math.sin(angle)
        
        for point in self.points:
            angle = (math.pi/2) - math.atan((point[1]-collision_point[1])/(point[0]-collision_point[0]))
            point_force += body_torque / (self.distance_between_points(collision_point,point)*math.sin(angle))
            self.points_velocity[self.points.index(point)] = np.array([point_force*math.cos(angle)/self.point_mass,point_force*math.sin(angle)/self.point_mass])
            
        

    def distance_between_points(self,point1,point2):
        return np.linalg.norm([point1[0]-point2[0],point1[1]-point2[1]])


    def check_collisions(self,line,point):
       
        # use the formula of the distance from a line to a point
        distance = abs((line[1][0]-line[0][0])*(line[0][1]-point[1])-(line[0][0]-point[0])*(line[1][1]-line[0][1]))/np.linalg.norm([line[1][0]-line[0][0],line[1][1]-line[0][1]])
        return distance
