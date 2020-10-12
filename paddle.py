import pygame
from constants import P_WIDTH, P_HEIGHT, WHITE, HEIGHT, RADIUS, L_PADDLE_X, R_PADDLE_X
from math import radians, cos, sin

class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT // 2
        self.w = P_WIDTH
        self.h = P_HEIGHT
        self.points = 0
        if self.x == L_PADDLE_X:
            self.left = True
        elif self.x == R_PADDLE_X:
            self.left = False

    def draw(self, win):
        paddle_sur = pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.h))
        pygame.display.update(paddle_sur)

    def ball_hit(self, ball):
        if self.left:
            if self.x <= ball.x <= self.x + P_WIDTH:
                if self.y <= ball.y <= self.y + P_HEIGHT:
                    angle = self.map(ball, -45)
                    ball.xspeed = ball.vel * cos(angle)
                    ball.yspeed = ball.vel * sin(angle)
                    ball.x = self.x + P_WIDTH + RADIUS
        else:
            if self.x <= ball.x <= self.x + P_WIDTH:
                if self.y <= ball.y <= self.y + P_HEIGHT:
                    angle = self.map(ball, -135)
                    ball.xspeed = ball.vel * cos(angle)
                    ball.yspeed = ball.vel * sin(angle) 
                    ball.x = self.x - RADIUS
        

    def map(self, ball, angle):
        diff = ball.y - self.x
        h = P_HEIGHT // 8
        i = 1
        while True:
            if self.y + (h * (i-1)) < ball.y < self.y + (h * (i)):
                if self.left:
                    angle += (15*(i-1))
                else:
                    angle -= (15*(i-1))
                break
            i += 1
        return radians(angle)
