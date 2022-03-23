
#####

# Tutorial: http://codingwithruss.com/pygame/flappy/background.html

#####

import random
import pygame
from pygame.locals import *

from bird import Bird
from button import Button
from pipe import Pipe

#initialize pygame
pygame.init()

clock = pygame.time.Clock()
fps = 60


screen_width= 864
screen_height = 936

#setting screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)

#define colours
white = (255, 255, 255)



#load images
bg = pygame.image.load('assets/bg.png')
ground_img = pygame.image.load('assets/ground.png')
button_img = pygame.image.load('assets/restart.png')


#define game variables
ground_scroll = 0
scroll_speed = 4

game_over = False
flying = False
score = 0
pass_pipe = False


pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score

#groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()


flappy = Bird(100, int(screen_height / 2))

#create restart button instance
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)


bird_group.add(flappy)

#game loop
run = True
while run:

    clock.tick(fps)

    #drawing background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update(game_over, flying)
    pipe_group.draw(screen)

    #drawing ground
    screen.blit(ground_img, (ground_scroll, 768))

    #check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
            and pass_pipe == False:
            pass_pipe = True

        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False


    draw_text(str(score), font, white, int(screen_width / 2), 20)    



    #look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    #check if bird has hit the ground
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if game_over == False and flying == True:

        #generate pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)

            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)

            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)

            last_pipe = time_now

        #draw and scroll the ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        
        pipe_group.update(scroll_speed)


    #check for game over and reset
    if game_over == True:
        if button.draw(screen) == True:
            game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and flying == False and game_over == False:
            flying = True

        


    pygame.display.update()

pygame.quit()