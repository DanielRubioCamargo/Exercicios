from matplotlib import animation
import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images") 

SCREEN_WIDTH = 540
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
FPS = 60

backgroundImage = pygame.image.load(os.path.join(imageDir,"BackgroundFB.png"))
backgroundImage = pygame.transform.scale(backgroundImage,(SCREEN_WIDTH,SCREEN_HEIGTH))

spriteDefaultSize = 96

spritesheet = pygame.image.load(os.path.join(imageDir,"SpritesheetFB.png"))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.verticalSpeed = 25
        self.jumpSpeed = -15
        self.gravity = 1
        self.currentIndex = 0
        self.initialXpos = 200
        self.initialYpos = (SCREEN_HEIGTH/2) - (spriteDefaultSize/2)
        self.animationFrames = list()
        for i in range(3):
            self.img = spritesheet.subsurface((i*spriteDefaultSize,0),(spriteDefaultSize,spriteDefaultSize))
            self.img = pygame.transform.scale(self.img,(48,48))
            self.animationFrames.append(self.img)
        self.image = self.animationFrames[self.currentIndex]
        self.rect = self.image.get_rect()
        self.rect.x = self.initialXpos
        self.rect.y = self.initialYpos

    def update(self):
        if self.currentIndex > 2.4:
            self.currentIndex = 0
        self.image = self.animationFrames[int(self.currentIndex)]
        self.currentIndex += 0.1

        self.verticalSpeed += self.gravity
        self.rect.y += self.verticalSpeed
        
    def jump(self):
        self.verticalSpeed = self.jumpSpeed
        

spriteGroup = pygame.sprite.Group()
bird = Bird()
spriteGroup.add(bird)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.jump()
    
    screen.blit(backgroundImage,(0,0))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()
