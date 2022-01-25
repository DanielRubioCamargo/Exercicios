from locale import currency
import pygame
from pygame.locals import *
from sys import exit
import os

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
        self.rect.center = (100,100)

    def update(self):
        self.currentIndex += 0.2
        if self.currentIndex > 2:
            self.currentIndex = 0
        self.image = self.dinoList[int(self.currentIndex)]

allSprites = pygame.sprite.Group()
dino = Dino()
allSprites.add(dino)

frameRate = pygame.time.Clock()

while True:
    frameRate.tick(30)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    allSprites.draw(screen)
    allSprites.update()

    pygame.display.flip()