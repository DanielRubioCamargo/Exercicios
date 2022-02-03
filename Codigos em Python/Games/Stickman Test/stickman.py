# libs
import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

'''
mainFile = os.path.dirname(__file__)
imageFile = os.path.join(mainFile,"images")
'''

spritesheet = pygame.image.load("Codigos em Python\\Games\\Stickman Test\\images\\Test Pixel Arts.png")
spriteSize = 32

# functions

# classes

class Player(pygame.sprite.Sprite()):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = spriteSize
        self.heigth = spriteSize
        self.playerIdleFrames = list()
        self.playerRunningFrames = list()
        self.playerJumpingFrame = spritesheet.subsurface((spriteSize*4,0),(spriteSize,spriteSize))
        # idle
        for i in range(2):
            self.img = spritesheet.subsurface((spriteSize*i,0),(spriteSize,spriteSize))
            self.img = pygame.transform.scale(self.img,(spriteSize*2,spriteSize*2))
            self.playerIdleFrames.append(self.img)
        # running
        for i in range(2,4):
            self.img = spritesheet.subsurface((spriteSize*i,0),(spriteSize,spriteSize))
            self.img = pygame.transform.scale(self.img,(spriteSize*2,spriteSize*2))
            self.playerRunningFrames.append(self.img)
        self.idleIndex = 0
        self.runningIndex = 0
        self.image = self.playerIdleFrames[self.idleIndex]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 500
        self.rect.y = SCREEN_HEIGTH - 100

    def update(self):
        pass

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Stickman Game")

# background image
backgroundImage = pygame.image.load("Codigos em Python\\Games\\Stickman Test\\images\\background.gif")
backgroundImage = pygame.transform.scale(backgroundImage,(SCREEN_WIDTH,SCREEN_HEIGTH))

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(backgroundImage,(0,0))
    pygame.display.flip()
