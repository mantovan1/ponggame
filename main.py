import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 600
height = 400

p1_x = 20
p1_y = 220
p1_goals = 0

p2_x = 510
p2_y = 160
p2_goals = 0

ball_x = 295
ball_y = 195

speed_x = 1
speed_y = 1

font = pygame.font.SysFont('arial', 20, bold=True, italic=True)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pong')
clock = pygame.time.Clock()

while True:

    clock.tick(200)
    screen.fill((0, 0, 0))

    message_p1 = f'player 1: {p1_goals}'
    message_p2 = f'player 2: {p2_goals}'

    formated_text_p1 = font.render(message_p1, False, (255, 255, 255))
    formated_text_p2 = font.render(message_p2, False, (255, 255, 255))

    for event in pygame.event.get():

        if event.type == QUIT:

                pygame.quit()

                exit()

    if pygame.key.get_pressed()[K_w]:

        if not p1_y+1 < 1:

            p1_y = p1_y - 1

    if pygame.key.get_pressed()[K_s]:

        if not p1_y+1 > 400 - 40:

            p1_y = p1_y + 1

    if pygame.key.get_pressed()[K_UP]:

        if not p2_y+1 < 1:

            p2_y = p2_y - 1

    if pygame.key.get_pressed()[K_DOWN]:

        if not p2_y+1 > 400 - 40:

            p2_y = p2_y + 1

    ball_x = ball_x - speed_x
    ball_y = ball_y - speed_y

    if ball_x < 1:

        ball_x = 295
        ball_y = 195
        speed_y = -speed_y
        p2_goals += 1

    if ball_x > 600 - 10:

        ball_x = 295
        ball_y = 195
        speed_y = -speed_y
        p1_goals += 1

    if ball_y < 1 or ball_y > 400 - 10:

        speed_y = -speed_y

    p1 = pygame.draw.rect(screen, (255, 0, 0), (p1_x, p1_y, 20, 40))
    p2 = pygame.draw.rect(screen, (0, 0, 255), (p2_x, p2_y, 20, 40))
    ball = pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, 10, 10))

    if ball.colliderect(p1) or ball.colliderect(p2):

        speed_x = -speed_x

    screen.blit(formated_text_p1, (10, 10))
    screen.blit(formated_text_p2, (10, 30))

    pygame.display.update()
