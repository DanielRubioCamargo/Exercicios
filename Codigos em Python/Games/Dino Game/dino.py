from locale import currency
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

mainFile = os.path.dirname(__file__)
imageFile = os.path.join(mainFile,"imagens")
soundFile = os.path.join(mainFile,"sons")

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480

WHITE = (255,255,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption('Dino Game')

spriteSheet = pygame.image.load(os.path.join(imageFile,"dinoSpritesheet.png"))

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dinoList = list()
        for i in range(3):
            self.img = spriteSheet.subsurface((i*32,0),(32,32))
            self.img = pygame.transform.scale(self.img,(32*3,32*3))
            self.dinoList.append(self.img)
        self.currentIndex = 0
        self.image = self.dinoList[self.currentIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (100,360)

    def update(self):
        self.currentIndex += 0.2
        if self.currentIndex > 2:
            self.currentIndex = 0
        self.image = self.dinoList[int(self.currentIndex)]

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((7*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*3,32*3))
        self.rect = self.image.get_rect()
        self.rect.x = (randrange(SCREEN_WIDTH,SCREEN_WIDTH+96,32))

    def update(self):
        if self.rect.x < -40:
            self.rect.x = (randrange(SCREEN_WIDTH,SCREEN_WIDTH+200,32))
        self.rect.x -= 10

allSprites = pygame.sprite.Group()
dino = Dino()
for i in range(3):
    cloud = Clouds()
    cloud.rect.y = i*60
    allSprites.add(cloud)
allSprites.add(dino)

frameRate = pygame.time.Clock()

while True:
    frameRate.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    allSprites.draw(screen)
    allSprites.update()

    pygame.display.flip()