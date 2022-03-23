import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.index = 0
        self.flap_speed = 0
        for num in range(1, 4):
            img = pygame.image.load(f'assets/bird{num}.png')
            self.images.append(img)
        self.image  = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.clicked = False

    
    def update(self, game_over, flying):

        if flying == True:
            #gravity 
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8 #stoping after touching the ground

            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)

        if game_over  == False:
            #jumping
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE] and self.clicked == False: 
                self.clicked = True 
                self.velocity -= 12

            if keys[pygame.K_SPACE] == 0:
                self.clicked = False

            #handle animation
            self.flap_speed +=1
            flap_cooldown = 5

            if self.flap_speed > flap_cooldown:
                self.flap_speed = 0
                self.index +=1

                if self.index >= len(self.images):
                    self.index = 0

            self.image = self.images[self.index]

            #rotation
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
