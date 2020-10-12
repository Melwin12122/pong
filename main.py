import pygame
from constants import *
from paddle import Paddle
from ball import Ball


pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
clock.tick(FPS)

# Fonts
F_NAME = pygame.font.SysFont("comicsans", 35)
F_POINT = pygame.font.SysFont("comicsans", 30)

ball = Ball()
Lpaddle = Paddle(L_PADDLE_X)
Rpaddle = Paddle(R_PADDLE_X)

def display(text, font, x, y, colour):
    t_surface = font.render(text, True, colour)
    WIN.blit(t_surface, (x, y))

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        bg = WIN.fill(BLACK)
        
        keys = pygame.key.get_pressed()
        # Right paddle
        if keys[pygame.K_UP] and Rpaddle.y > 0:
                Rpaddle.y -= P_VEL
        elif keys[pygame.K_DOWN] and Rpaddle.y + P_HEIGHT < HEIGHT:
            Rpaddle.y += P_VEL
        # Left paddle
        if keys[pygame.K_w] and Lpaddle.y > 0:
            Lpaddle.y -= P_VEL
        elif keys[pygame.K_s]and Lpaddle.y + P_HEIGHT < HEIGHT:
            Lpaddle.y += P_VEL

        Lpaddle.ball_hit(ball)
        Rpaddle.ball_hit(ball)

        ball.out_of_bound(Lpaddle, Rpaddle)
        
        Lpaddle.draw(WIN)
        Rpaddle.draw(WIN)
        ball.draw(WIN)
        display(str(Lpaddle.points), F_POINT, L_SCORE_X, SCORE_Y, GREEN)
        display(str(Rpaddle.points), F_POINT, R_SCORE_X, SCORE_Y, GREEN)

        pygame.display.update(bg)

main()
pygame.quit()
