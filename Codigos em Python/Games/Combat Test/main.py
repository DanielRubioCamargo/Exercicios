import pygame
from pygame.locals import *
import sys
import os

pygame.init()

mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

spritesheet = pygame.image.load(os.path.join(imageDir,"spritesheet.png"))

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))

clock = pygame.time.Clock()
FPS = 30

class Warrior(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.combatList = list()
        self.currentIndex = 0
        for i in range(6):
            self.img = spritesheet.subsurface((i*96,0),(96,96))
            self.combatList.append(self.img)
        self.image = self.combatList[self.currentIndex]
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 250

    def update(self):
        if self.currentIndex > 5:
            self.currentIndex = 0
        self.image = self.combatList[int(self.currentIndex)]
        self.currentIndex += 0.5

class Wizard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.combatList = list()
        self.currentIndex = 0
        for i in range(3):
            self.img = spritesheet.subsurface((i*96,96),(96,96))
            self.combatList.append(self.img)
        self.image = self.combatList[self.currentIndex]
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 250

    def update(self):
        if self.currentIndex > 2.4:
            self.currentIndex = 0
        self.image = self.combatList[int(self.currentIndex)]
        self.currentIndex += 0.1
    
spriteGroup = pygame.sprite.Group()
warrior = Warrior()
wizard = Wizard()
spriteGroup.add(warrior)
spriteGroup.add(wizard)

while True:
    screen.fill((255,255,255))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()