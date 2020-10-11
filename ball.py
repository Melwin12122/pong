import pygame
from constants import RADIUS, RED, WIDTH, HEIGHT, VELOCITY
from math import pi, cos, sin
from random import uniform
from time import time

class Ball:
    def __init__(self):
        self.r = RADIUS
        self.vel = VELOCITY
        self.time = None
        self.reset()

    def draw(self, win):
        if self.time is None or time() - self.time > 3:
            self.update()
            self.time = None
        ball_sur = pygame.draw.circle(win, RED, (int(self.x), int(self.y)), self.r)
        pygame.display.update(ball_sur)

    def update(self):
        self.hit_wall()
        self.x += self.xspeed
        self.y += self.yspeed

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = uniform(-pi/4, pi/4)
        self.xspeed = self.vel * cos(self.angle)
        self.yspeed = self.vel * sin(self.angle)
        if(uniform(0, 1) < 0.5):
            self.xspeed *= -1

    def out_of_bound(self, lpad, rpad):
        if self.x - self.r > WIDTH:
            self.reset()
            lpad.points += 1
            self.time = time()
        elif self.x + self.r < 0:
            self.reset()
            rpad.points += 1
            self.time = time()
        
        
    def hit_wall(self):
        if self.y < self.r or self.y + self.r > HEIGHT:
            self.yspeed *= -1 
